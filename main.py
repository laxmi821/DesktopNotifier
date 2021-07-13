from plyer import notification


#specify the parameters
title = 'Hey There'

message= 'Thankyou for reading! Take care!'

notification.notify(title= title,
                    message= message,
                    app_icon = None,
                    timeout= 10,
                    toast=False)
