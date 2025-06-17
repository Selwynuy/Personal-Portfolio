"""
Views for the main app.
"""
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .models import Project, SkillCategory, Timeline
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.contrib import messages
from apps.core.utils import send_email
import logging

logger = logging.getLogger(__name__)


def home(request):
    # Fetch data for the about section
    skill_categories = SkillCategory.objects.prefetch_related('skills').all()
    timeline_events = Timeline.objects.all().order_by('-date')
    projects = Project.objects.all()
    years = Timeline.objects.dates('date', 'year', order='DESC')
    context = {
        'skill_categories': skill_categories,
        'timeline_events': timeline_events,
        'projects': projects,
        'years': years,
    }
    return render(request, 'main/home.html', context)


def contact(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        message = request.POST["message"]

        # Format the message
        formatted_message = f"""
        New contact form submission:
        
        From: {name} ({email})
        
        Message:
        {message}
        """

        # Send email using Supabase
        try:
            response = send_email(
                to_email="uywenwen@gmail.com",  # Your email
                subject=f"Portfolio Contact: Message from {name}",
                message=formatted_message
            )
            logger.info(f"Email send response: {response}")
            
            if response:
                messages.success(request, "Your message has been sent successfully!")
            else:
                messages.error(request, "Sorry, there was an error sending your message. Please try again later.")
        except Exception as e:
            logger.error(f"Error sending email: {str(e)}")
            messages.error(request, "Sorry, there was an error sending your message. Please try again later.")

        return redirect("main:home")

    return render(request, "main/contact.html")


def timeline_events_ajax(request):
    year = request.GET.get('year')
    if year and year != 'all':
        events = Timeline.objects.filter(date__year=year).order_by('-date')
    else:
        events = Timeline.objects.all().order_by('-date')
    html = render_to_string('components/timeline_events.html', {'timeline_events': events})
    return JsonResponse({'html': html}) 