from chat.models import Chat


def is_chat_unique(item_id, sender_id, receiver_id):
    """
    Проверка чата, при создании, на уникальность
    Проверка отправителя получателя и вещи
    """
    chat1 = Chat.objects.filter(Q(item=item_id) & Q(sender_id=sender_id) & Q(receiver_id=receiver_id)).first()
    chat2 = Chat.objects.filter(Q(item=item_id) & Q(sender_id=receiver_id) & Q(receiver_id=sender_id)).first()
    if chat1:
        return chat1.id
    elif chat2:
        return chat2.id
    return False