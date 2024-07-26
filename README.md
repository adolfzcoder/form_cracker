# Form Cracker
 This uses a more primitive but still effective method using pyautogui to crack codes in HTML forms, NO REQUESTS USED

 To get started, clone the reprository, then Install pyautogui `pip install pyautogui`
 Then use the `get_pos()` function to find the location (coordinates) of the field you would like to crack, Also to find the submit button Coordinates

After finding the coordinates, define how a succesful and an unsuccesful request looks like.
Use `gui.locateOnScreen('icon.png', confidence=0.6, grayscale=True` to find the message/result from an unsuccesful request.

This code is for simple forms and can be optimized using requests, but for website that don't allow bots/automation this would be the next thing to use
