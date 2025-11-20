from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import JsonResponse
import json
import re
from django.views.decorators.csrf import csrf_exempt
import google.generativeai as genai
from .models import Contact,ContactForm,Feature,Working,Discliamer
# Create your views here.




@csrf_exempt
def health_chatbot(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_input = data.get('message', '').strip()

            # 👋 Default message if user_input is empty
            if not user_input:
                return JsonResponse({
                    "reply": "👋 Hello! I’m your Health Assistant. How can I help you today?"
                })

            # ✅ Initialize Gemini model
            # genai.configure(api_key="")
            genai.configure(api_key="AIzaSyDWsxAfxNcp3ffzrEowjFcCN7dFYnVakNk")
            model = genai.GenerativeModel("gemini-2.5-flash")

            # 🧠 Generate AI response
            prompt = f"""
            You are a friendly and professional AI health assistant.
            User's question: "{user_input}"
            
            Please give your answer in clean readable format with:
            - Short paragraphs
            - Bullet points for lists
            - Clear line breaks between ideas
            Avoid using markdown syntax like ** or ##.
            """
            response = model.generate_content(prompt)

            if not response or not hasattr(response, "text"):
                formatted_reply = "⚠️ No response from Gemini."
            else:
                reply_text = response.text.strip()

                # 🧹 Basic cleaning & formatting
                reply_text = re.sub(r"\*\*(.*?)\*\*", r"<b>\1</b>", reply_text)  # bold markdown
                reply_text = re.sub(r"^- ", "• ", reply_text, flags=re.MULTILINE)  # bullet points
                reply_text = reply_text.replace("\n", "<br>")  # line breaks

                formatted_reply = reply_text

            return JsonResponse({"reply": formatted_reply})


            # return JsonResponse({"reply": reply_text})

        except Exception as e:
            return JsonResponse({"reply": f"Error: {str(e)}"})

    # 👋 Default message for GET requests
    return JsonResponse({
        "reply": "👋 Hello! I’m your Health Assistant. How can I help you today?"
    })





def home(request):
    feature_infos=Feature.objects.all()
    print("FEATURES FROM DB:",feature_infos)
    working_infos=Working.objects.all()
    print("WORKING FROM DB:",working_infos)
    disclaimer_infos=Discliamer.objects.all()
    print("DISCLAIMER FROM DB",disclaimer_infos )

    return render(request, 'index.html',{
        'feature_infos':feature_infos,
        'working_infos':working_infos,
        'disclaimer_infos':disclaimer_infos
        })



def contact(request):
    success=False
    if request.method=='POST':
        name=request.POST.get('name')
        age=request.POST.get('age')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        message=request.POST.get('message')

        ContactForm.objects.create(
            name=name,
            age=age,
            email=email,
            phone=phone,
            message=message,
        )
       
        messages.success(request, "your message has been sent successfully. we will contaact you soon." )
    
        return redirect('contact')


    contact_infos=Contact.objects.all()

    return render(request, 'contact.html',{'success':success,'contact_infos':contact_infos})



