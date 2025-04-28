from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Message
from .forms import MessageForm
from django.contrib import messages

def inbox(request):
    messages_list = Message.objects.filter(receiver=request.user).order_by('-created_at')
    return render(request, 'messenger/inbox.html', {'messages_list': messages_list})


@login_required
def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.save()
            return redirect('inbox')
    else:
        form = MessageForm()
    return render(request, 'messenger/send_messages.html', {'form': form})

@login_required
def sent_messages(request):
    sent_messages_list = Message.objects.filter(sender=request.user).order_by('-created_at')
    return render(request, 'messenger/sent_messages.html', {'sent_messages_list': sent_messages_list})


@login_required
def sent_message_detail(request, pk):
    message = get_object_or_404(Message, pk=pk, sender=request.user)
    return render(request, 'messenger/sent_message_detail.html', {'message': message})

@login_required
def message_detail(request, pk):
    message = get_object_or_404(Message, pk=pk)

    if request.user != message.receiver:
        return redirect('inbox')

    return render(request, 'messenger/message_detail.html', {'message': message})




@login_required
def message_delete(request, pk):
    message = get_object_or_404(Message, pk=pk)
    if request.method == 'POST':
        message.delete()
        messages.success(request, 'Mensaje eliminado exitosamente.')
        return redirect('inbox')
    return render(request, 'messenger/message_confirm_delete.html', {'message': message})

