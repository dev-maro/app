import flet as ft

def main(page: ft.Page):
    display = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=300, read_only=True)
    
    # Define buttons and layout
    buttons = [
        "7", "8", "9", "/",
        "4", "5", "6", "*",
        "1", "2", "3", "-",
        "C", "0", "=", "+"
    ]
    
    def button_click(event):
        current_value = display.value
        button_text = event.control.text
        
        if button_text == "C":
            display.value = "0"
        elif button_text == "=":
            try:
                display.value = str(eval(current_value))
            except Exception:
                display.value = "Error"
        else:
            if current_value == "0" or display.value == "Error":
                display.value = button_text
            else:
                display.value += button_text
        
        page.update()
    
    # Use 'TextButton' if 'Button' is not available
    button_controls = [ft.TextButton(text=btn, on_click=button_click) for btn in buttons]
    
    rows = [ft.Row(controls=button_controls[i:i+4]) for i in range(0, len(button_controls), 4)]
    
    page.add(
        display,
        *rows
    )

# Run the app
ft.app(target=main)

