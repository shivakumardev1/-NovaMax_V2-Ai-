import webbrowser

def prepare_whatsapp(contact, message):
    # WhatsApp Web authentication and the final send remain user-controlled.
    webbrowser.open("https://web.whatsapp.com/")
    return (
        f"WhatsApp Web khol diya hai. {contact} ko ye message bhejna tha: "
        f"{message}. Final send tum manually confirm karo."
    )
