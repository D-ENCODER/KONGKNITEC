# # Date    : 01/10/22 9:25 am
# # Author  : dencoder (hetcjoshi1684@gmail.com)
# # GitHub    : (https://github.com/D-ENCODER)
# # Twitter    : (https://twitter.com/Hetjoshi1684)
# # Version : 1.0.0
# import customtkinter as ctk
# import configure
# from Helper_Functions.load_image import load_image
#
#
# class SplashScreen(ctk.CTkFrame):
#     def __init__(self, **kwargs):
#         ctk.CTkFrame.__init__(self, kwargs['parent'], fg_color=configure.hover_color)
#         self._controller = kwargs['controller']
#         kwargs['parent'].grid_configure(padx=(configure.screen_width - 450) / 2)
#         self._img = load_image(self, 'Icons/logo.png', 140)
#         self._splashGUI()
#
#     def _splashGUI(self):
#         self.icon = ctk.CTkFrame(self, fg_color=configure.hover_color)
#         self.iconimg = ctk.CTkLabel(master=self.icon, image=self._img, anchor='center')
#         self.icon.grid(row=0, column=0)
#
#         def fade_in(self):
#             alpha = self.parent.attributes("-alpha")
#             print(alpha)
#             if alpha < 1:
#                 alpha += .1
#                 self.parent.attributes("-alpha", alpha)
#                 self.after(100, self.fade_in)
#             else:
#                 pass
#
#         def fade_away(self):
#             alpha = self.parent.attributes("-alpha")
#             print(alpha)
#             if alpha > 0:
#                 alpha -= .1
#                 self.parent.attributes("-alpha", alpha)
#                 self.after(100, self.fade_away)
#             else:
#                 self.parent.destroy()
#
#         self.icon.attributes("-alpha", 0)
#         self.label = ctk.CTkLabel(master=self, text='Kongknitec', text_font=(configure.font, 60), anchor='center',
#                                   text_color=configure.dominant_color)
#         self.label.grid(row=1, column=0)
#         self.label.attributes("-alpha", 0)
