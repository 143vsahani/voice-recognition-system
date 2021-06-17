from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
import json
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
import requests
from kivy.core.window import Window

Window.size=(412, 732)



help_str = '''
#:import MagicBehavior kivymd.uix.behaviors.MagicBehavior

ScreenManager:
    WelcomeScreen:
    MainScreen:
    LoginScreen:
    SignupScreen:
    VoiceScreen:
    AboutScreen:
    ExtraScreen:
<WelcomeScreen>:
    name:'welcomescreen'
    Image:
        source: 'front.png'
        allow_stretch: True
    MDRaisedButton:
        text:'Login'
        pos_hint : {'center_x':0.3,'center_y':0.3}
        size_hint: (0.3,0.07)
        on_press: 
            root.manager.current = 'loginscreen'
            root.manager.transition.direction = 'left'
    MDRaisedButton:
        text:'Signup'
        pos_hint : {'center_x':0.7,'center_y':0.3}
        size_hint: (0.3,0.07)
        on_press:
            root.manager.current = 'signupscreen'
            root.manager.transition.direction = 'left'
        
<LoginScreen>:
    name:'loginscreen'
    Image:
        source: 'login.jpg'
        allow_stretch: True
    MDLabel:
        text:'Login'
        font_style:'H2'
        halign:'center'
        text_color: 0,255,255,1 
        pos_hint: {'center_y':0.9}
    MDTextField:
        
        id:login_email
        pos_hint: {'center_y':0.6,'center_x':0.5}
        size_hint : (0.7,0.1)
        hint_text: 'Email'
        helper_text:'Required'
        helper_text_mode:  'on_error'
        icon_right: 'account'
        icon_right_color: app.theme_cls.primary_color
        required: True
        mode: "rectangle"
    MDTextField:
        id:login_password
        pos_hint: {'center_y':0.4,'center_x':0.5}
        size_hint : (0.7,0.1)
        hint_text: 'Password'
        helper_text:'Required'
        helper_text_mode:  'on_error'
        icon_right: 'account'
        icon_right_color: app.theme_cls.primary_color
        required: True
        mode: "rectangle"
    MDRaisedButton:
        text:'Login'
        size_hint: (0.3,0.07)
        pos_hint: {'center_x':0.5,'center_y':0.2}
        on_press:
            app.login()
            app.username_changer() 
            
        
    MDTextButton:
        text: 'Create an account'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press:
            root.manager.current = 'signupscreen'
            root.manager.transition.direction = 'up'
<SignupScreen>:
    name:'signupscreen'
    Image:
        source: 'signup.jpg'
        allow_stretch: True
    MDLabel:
        text:'SignUp'
        font_style:'H2'
        halign:'center'
        text_color:0,255,255,0
        pos_hint: {'center_y':0.9}
    
    MDTextField:
        id:signup_username
        pos_hint: {'center_y':0.62,'center_x':0.5}
        size_hint : (0.7,0.1)
        hint_text: 'Username'
        helper_text:'Required'
        helper_text_mode:  'on_error'
        icon_right: 'account'
        icon_right_color: app.theme_cls.primary_color
        required: True
        mode: "rectangle"
    
    MDTextField:
        id:signup_email
        pos_hint: {'center_y':0.5,'center_x':0.5}
        size_hint : (0.7,0.1)
        hint_text: 'Email'
        helper_text:'Required'
        helper_text_mode:  'on_error'
        icon_right: 'email-variant'
        icon_right_color: app.theme_cls.primary_color
        required: True
        mode: "rectangle"
    MDTextField:
        id:signup_password
        pos_hint: {'center_y':0.38,'center_x':0.5}
        size_hint : (0.7,0.1)
        hint_text: 'Password'
        helper_text:'Required'
        helper_text_mode:  'on_error'
        icon_right: 'lock'
        icon_right_color: app.theme_cls.primary_color
        required: True
        mode: "rectangle"
    MDRaisedButton:
        text:'Signup'
        size_hint: (0.3,0.07)
        pos_hint: {'center_x':0.5,'center_y':0.2}
        on_press: app.signup()
    MDTextButton:
        text: 'Already have an account'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press:
            root.manager.current = 'loginscreen'
            root.manager.transition.direction = 'down'
    
    
<MainScreen>:
    name: 'mainscreen'
    Image:
        source: 'login.jpg'
        allow_stretch: True
    MDLabel:
        id:username_info
        text:'Hello Main'
        font_style:'H5'
        halign:'center'
        pos_hint: {'center_y':0.9}
    MDLabel:
        text:"Welcom to I-secure"
        pos_hint:{"center_y": .95}
        font_style:"H4"
        halign:"center"
        theme_text_color:"Custom"
        text_color:0,0,0,1
    MDRaisedButton:
        text:"voice-model"
        pos_hint:{"center_x": .5,"center_y":.5}
        size_hint_x:.8
        theme_text_color:"Custom" 
        on_press:
            root.manager.current="voice"
            root.manager.transition.direction = 'left' 
    MDRaisedButton:
        text:"Extra Features"
        pos_hint:{"center_x": .5,"center_y":.4}
        size_hint_x:.8
        theme_text_color:"Custom" 
        on_press:
            root.manager.current="extra"
            root.manager.transition.direction = 'left' 
    MDRaisedButton:
        text: "about us"
        pos_hint:{"center_x": .5,"center_y":.3}
        size_hint_x:.8
        theme_text_color:"Custom"
        on_press:
            root.manager.current="about"
            root.manager.transition.direction = 'up'
    MDRoundFlatButton:
        text: "Log Out"
        size_hint_x:.3
        pos_hint: {"center_x": .8, "center_y": .1}
        on_press:
            root.manager.current = 'loginscreen'
            root.manager.transition.direction = 'down'
        
    
<VoiceScreen>:
    name:"voice"
    MDFloatLayout:
    Image:
        source: 'login.jpg'
        allow_stretch: True
    MDLabel:
        text:"Welcom to I-secure"
        pos_hint:{"center_y": .95}
        font_style:"H4"
        halign:"center"
        theme_text_color:"Custom"
        text_color:0,0,0,1

    MDLabel:
        text:"voice module"
        pos_hint:{"center_y": .85}
        font_style:"H5"
        halign:"center"
        theme_text_color:"Custom"
        text_color:0,0,0,1  

    MDTextField:
       
        hint_text:"enter your key1"
        pos_hint:{"center_x": .3,"center_y":.6}
        current_hint_text_color:0,0,0,1
        size_hint_x:.4
    MDTextField:
        
        hint_text:"enter your key2"
        pos_hint:{"center_x": .3,"center_y":.5}
        current_hint_text_color:0,0,0,1
        size_hint_x:.4
    MDTextField:
        
        hint_text:"enter yor phon1"
        pos_hint:{"center_x": .8,"center_y":.6}
        current_hint_text_color:0,0,0,1
        size_hint_x:.4
    MDTextField:
        
        hint_text:"enter yor phon2"
        pos_hint:{"center_x": .8,"center_y":.5}
        current_hint_text_color:0,0,0,1
        size_hint_x:.4            
    
    MDRaisedButton:
        text: "save"
        pos_hint:{"center_x": .5,"center_y":.3}
        size_hint_x:.5
        theme_text_color:"Custom"
    MDRaisedButton:
        text: "back"
        pos_hint:{"center_x": .5,"center_y":.1}
        size_hint_x:.5
        on_press:
            root.manager.current="mainscreen" 
            root.manager.transition.direction = 'right'
<AboutScreen>:
    name:"about"
    MDFloatLayout:
    Image:
        source: 'signup.jpg'
  
            # Giving the size of image
        
  
            # allow sterching of image 
        allow_stretch: True
    MDLabel:
        text:"About-Us"
        pos_hint:{"center_y": .95}
        font_style:"H4"
        halign:"center"
        theme_text_color:"Custom"
        text_color:0,0,0,1
    MDCard :

        size_hint : None,None
        size : 320,400
        pos_hint : {"center_x":.5,"center_y":.5}
        elevation : 15
        md_bg_color : app.theme_cls.primary_color
        padding : 20
        spacing : 30
        orientation : "vertical"
    
        MDLabel:
            text:"we are a group of highly motivated computer science students and our goal to make this world more intersting then it is by our develpment."
            pos_hint:{"center_y": .6}
            font_style:"H4"
            halign:"center"
            theme_text_color:"Custom"
            text_color:0,0,0,1
    MDRaisedButton:
        text: "back"
        pos_hint:{"center_x": .5,"center_y":.1}
        size_hint_x:.5
        on_press:
            root.manager.current="mainscreen"
            root.manager.transition.direction = 'down'
<ExtraScreen>:
    name:"extra"
    MDFloatLayout:
    Image:
        source: 'login.jpg'
  
            # Giving the size of image
        
  
            # allow sterching of image 
        allow_stretch: True
    MDSwitch:
        pos_hint: {'center_x': .9, 'center_y': .85}
    
    MDSwitch:
        pos_hint: {'center_x': .9, 'center_y': .75}
    
    MDLabel:
        text:"desable power off button"
        pos_hint:{'center_x': .5,"center_y": .85}
        font_style:"Body1"
        halign:"center"
        theme_text_color:"Custom"
        text_color:0,0,0,1
  
    MDLabel:
        text:"desable aroplan on button"
        pos_hint:{'center_x': .5,"center_y": .75}
        font_style:"Body1"
        halign:"center"
        theme_text_color:"Custom"
        text_color:0,0,0,1  

    

    MDRaisedButton:
        text: "save"
        pos_hint:{"center_x": .5,"center_y":.5}
        size_hint_x:.5
        theme_text_color:"Custom"
        
    MDRaisedButton:
        text: "back"
        pos_hint:{"center_x": .5,"center_y":.1}
        size_hint_x:.5
        on_press:
            root.manager.current="mainscreen"
            root.manager.transition.direction = 'down'

'''


class WelcomeScreen(Screen):
    pass
class MainScreen(Screen):
    pass
class LoginScreen(Screen):
    pass
class SignupScreen(Screen):
    pass
class VoiceScreen(Screen):
    pass

class AboutScreen(Screen):
    pass
class ExtraScreen(Screen):
    pass

sm = ScreenManager()
sm.add_widget(WelcomeScreen(name = 'loginscreen'))
sm.add_widget(MainScreen(name = 'mainscreen'))
sm.add_widget(LoginScreen(name = 'loginscreen'))
sm.add_widget(SignupScreen(name = 'signupscreen'))
sm.add_widget(VoiceScreen(name='Voice')) 
sm.add_widget(AboutScreen(name='about')) 
sm.add_widget(AboutScreen(name='extra')) 


class LoginApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette="Blue"
        self.strng = Builder.load_string(help_str)
        self.url  = "https://loginsetup-66c8e-default-rtdb.firebaseio.com/.json"
        return self.strng

    def signup(self):
        signupEmail = self.strng.get_screen('signupscreen').ids.signup_email.text
        signupPassword = self.strng.get_screen('signupscreen').ids.signup_password.text
        signupUsername = self.strng.get_screen('signupscreen').ids.signup_username.text
        if signupEmail.split() == [] or signupPassword.split() == [] or signupUsername.split() == []:
            cancel_btn_username_dialogue = MDFlatButton(text = 'Retry',on_release = self.close_username_dialog)
            self.dialog = MDDialog(title = 'Invalid Input',text = 'Please Enter a valid Input',size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
            self.dialog.open()
        if len(signupUsername.split())>1:
            cancel_btn_username_dialogue = MDFlatButton(text = 'Retry',on_release = self.close_username_dialog)
            self.dialog = MDDialog(title = 'Invalid Username',text = 'Please enter username without space',size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
            self.dialog.open()
        else:
            print(signupEmail,signupPassword)
            signup_info = str({f'\"{signupEmail}\":{{"Password":\"{signupPassword}\","Username":\"{signupUsername}\"}}'})
            signup_info = signup_info.replace(".","-")
            signup_info = signup_info.replace("\'","")
            to_database = json.loads(signup_info)
            print((to_database))
            requests.patch(url = self.url,json = to_database)
            self.strng.get_screen('loginscreen').manager.current = 'loginscreen'
    auth = 'GzBbmfxFP0uOLoBFuMBNTsVB46uD1FgCPC21a6PH'

    def login(self):
        loginEmail = self.strng.get_screen('loginscreen').ids.login_email.text
        loginPassword = self.strng.get_screen('loginscreen').ids.login_password.text

        self.login_check = False
        supported_loginEmail = loginEmail.replace('.','-')
        supported_loginPassword = loginPassword.replace('.','-')
        request  = requests.get(self.url+'?auth='+self.auth)
        data = request.json()
        emails= set()
        for key,value in data.items():
            emails.add(key)
        if supported_loginEmail in emails and supported_loginPassword == data[supported_loginEmail]['Password']:
            self.username = data[supported_loginEmail]['Username']
            self.login_check=True
            self.strng.get_screen('mainscreen').manager.current = 'mainscreen'
        else:
            self.dialog = MDDialog(title = 'Invalid Input',text = 'Please Enter a valid Input',size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
            self.dialog.open()
            print("user no longer exists")
    def close_username_dialog(self,obj):
        self.dialog.dismiss()
    def username_changer(self):
        if self.login_check:
            self.strng.get_screen('mainscreen').ids.username_info.text = f" {self.username}"

LoginApp().run()
