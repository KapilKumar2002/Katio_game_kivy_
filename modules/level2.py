from kivy.properties import StringProperty,ListProperty
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.core.audio import SoundLoader
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFillRoundFlatButton, MDFillRoundFlatIconButton
from kivymd.app import MDApp
class GameFinishMessage(MDBoxLayout):
    textp= StringProperty()
    color = ListProperty()   

class Level2(MDScreen):
    dialog = None
    m = 0
    n = 0
    player1_color = [0, 0, 1, 1]
    player2_color = [1, 0, 0, 1]
    button_clicked = SoundLoader.load("assets/button.wav")
    shift_sound = SoundLoader.load("assets/shift.wav")
    winning_sound = SoundLoader.load("assets/winning.wav")

    def switching(self):
        b = self.ids.playb
        if (b.icon == "pause"):
            b.icon = "play"
            self.ids.common10.disabled = True
            self.ids.restore.disabled = True
            for i in range(1, 21):
                self.ids[f"p1{i}"].disabled = True
                self.ids[f'p1{i}'].disabled_color = self.ids[f'p1{i}'].text_color
            for j in range(1, 21):
                self.ids[f"p2{j}"].disabled = True
                self.ids[f"p2{j}"].disabled_color = self.ids[f'p2{j}'].text_color
        else:
            b.icon = "pause"
            self.ids.common10.disabled = False
            for i in range(1, 21):
                self.ids[f"p1{i}"].disabled = False
            for j in range(1, 21):
                self.ids[f"p2{j}"].disabled = False
            self.ids.restore.disabled = False

    def player1(self, first):
        y = 0.125
        x = 0.25
        self.button_clicked.play()
        for i in range(1, 21):
            if self.ids[f'p2{i}'].icon == "account": 
                self.ids[f'p2{i}'].disabled = True
                self.ids[f'p2{i}'].disabled_color = self.player2_color
        self.ids[f'common10'].text_color =  0,0.2,0.21,0.31
        for i in range(1, 21):
            if self.ids[f'p1{i}'].icon == "record-circle" or self.ids[f'p1{i}'].text_color == [245/255, 5/255, 237/255]:
                self.ids[f'p1{i}'].text_color = 0,0.2,0.21,0.31
        for i in range(1, 21):
            if self.ids[f'p2{i}'].icon == "record-circle" or self.ids[f'p2{i}'].text_color == [245/255, 5/255, 237/255]:
                self.ids[f'p2{i}'].text_color = 0,0.2,0.21,0.31
        self.p1 = first
        points = first.pos_hint
        pb_co = (points['center_x'], points['center_y'])
        if pb_co == (0, 2*y) or pb_co == (2*x, 0) or pb_co == (2*x, 2*y) or pb_co == (4*x, 2*y) or pb_co == (x, 3*y) or pb_co == (3*x, 3*y) or pb_co == (0, 4*y) or pb_co == (4*x, 4*y) or pb_co == (x, 5*y) or pb_co == (3*x, 5*y) or pb_co == (0, 6*y) or pb_co == (2*x, 6*y) or pb_co == (4*x, 6*y) or pb_co == (2*x, 4*y) or pb_co == (0,0)or pb_co==(2*x, 8*y) or pb_co == (4*x, 0) or pb_co==(0, 8*y) or pb_co==(4*x, 8*y):
            self.w_f_fi = (pb_co[0] - x, pb_co[1])
            self.e_f_fi = (pb_co[0]+x, pb_co[1])
            self.n_f_fi = (pb_co[0], pb_co[1]+y)
            self.s_f_fi = (pb_co[0], pb_co[1]-y)
            self.ne_f_fi = (pb_co[0] + x, pb_co[1] + y)
            self.nw_f_fi = (pb_co[0] - x, pb_co[1] + y)
            self.sw_f_fi = (pb_co[0] - x, pb_co[1] - y)
            self.se_f_fi = (pb_co[0] + x, pb_co[1] - y)
            self.xw_f_fi = (pb_co[0] - 2*x, pb_co[1])
            self.xe_f_fi = (pb_co[0]+ 2*x, pb_co[1])
            self.xn_f_fi = (pb_co[0], pb_co[1]+2*y)
            self.xs_f_fi = (pb_co[0], pb_co[1]-2*y)
            self.xne_f_fi = (pb_co[0] + 2*x, pb_co[1] + 2*y)
            self.xnw_f_fi = (pb_co[0] - 2*x, pb_co[1] + 2*y)
            self.xsw_f_fi = (pb_co[0] - 2*x, pb_co[1] - 2*y)
            self.xse_f_fi = (pb_co[0] + 2*x, pb_co[1] - 2*y)
            if self.ids.common10.pos_hint == {"center_x": self.w_f_fi[0], "center_y": self.w_f_fi[1]} or self.ids.common10.pos_hint == {"center_x": self.e_f_fi[0], "center_y": self.e_f_fi[1]} or self.ids.common10.pos_hint == {"center_x": self.s_f_fi[0], "center_y": self.s_f_fi[1]} or self.ids.common10.pos_hint == {"center_x": self.n_f_fi[0], "center_y": self.n_f_fi[1]} or self.ids.common10.pos_hint == {"center_x": self.sw_f_fi[0], "center_y": self.sw_f_fi[1]} or self.ids.common10.pos_hint == {"center_x": self.se_f_fi[0], "center_y": self.se_f_fi[1]} or self.ids.common10.pos_hint == {"center_x": self.nw_f_fi[0], "center_y": self.nw_f_fi[1]} or self.ids.common10.pos_hint == {"center_x": self.ne_f_fi[0], "center_y": self.ne_f_fi[1]}:
                self.ids.common10.text_color = 245/255, 5/255, 237/255
            for i in range(1, 21):
                if (self.ids[f'p2{i}'].pos_hint == {"center_x": self.w_f_fi[0], "center_y": self.w_f_fi[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.e_f_fi[0], "center_y": self.e_f_fi[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.s_f_fi[0], "center_y": self.s_f_fi[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.n_f_fi[0], "center_y": self.n_f_fi[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.sw_f_fi[0], "center_y": self.sw_f_fi[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.se_f_fi[0], "center_y": self.se_f_fi[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.nw_f_fi[0], "center_y": self.nw_f_fi[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.ne_f_fi[0], "center_y": self.ne_f_fi[1]}) and self.ids[f'p2{i}'].icon == "record-circle" and self.ids[f'p2{i}'].text_color == [0,0.2,0.21,0.31]:
                    self.ids[f'p2{i}'].text_color = 245/255, 5/255, 237/255
                if (self.ids[f'p1{i}'].pos_hint == {"center_x": self.w_f_fi[0], "center_y": self.w_f_fi[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.e_f_fi[0], "center_y": self.e_f_fi[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.s_f_fi[0], "center_y": self.s_f_fi[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.n_f_fi[0], "center_y": self.n_f_fi[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.sw_f_fi[0], "center_y": self.sw_f_fi[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.se_f_fi[0], "center_y": self.se_f_fi[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.nw_f_fi[0], "center_y": self.nw_f_fi[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.ne_f_fi[0], "center_y": self.ne_f_fi[1]}) and self.ids[f'p1{i}'].icon == "record-circle" and self.ids[f'p1{i}'].text_color == [0,0.2,0.21,0.31]:
                    self.ids[f'p1{i}'].text_color = 245/255, 5/255, 237/255
            for i in range(1, 21):
                if (self.ids[f'p2{i}'].pos_hint == {"center_x": self.w_f_fi[0], "center_y": self.w_f_fi[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.e_f_fi[0], "center_y": self.e_f_fi[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.s_f_fi[0], "center_y": self.s_f_fi[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.n_f_fi[0], "center_y": self.n_f_fi[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.ne_f_fi[0], "center_y": self.ne_f_fi[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.se_f_fi[0], "center_y": self.se_f_fi[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.sw_f_fi[0], "center_y": self.sw_f_fi[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.nw_f_fi[0], "center_y": self.nw_f_fi[1]}) and self.ids[f'p2{i}'].icon != "record-circle":
                    if self.ids.common10.pos_hint == {"center_x": self.xw_f_fi[0], "center_y": self.xw_f_fi[1]} or self.ids.common10.pos_hint == {"center_x": self.xe_f_fi[0], "center_y": self.xe_f_fi[1]} or self.ids.common10.pos_hint == {"center_x": self.xs_f_fi[0], "center_y": self.xs_f_fi[1]} or self.ids.common10.pos_hint == {"center_x": self.xn_f_fi[0], "center_y": self.xn_f_fi[1]} or self.ids.common10.pos_hint == {"center_x": self.xnw_f_fi[0], "center_y": self.xnw_f_fi[1]} or self.ids.common10.pos_hint == {"center_x": self.xsw_f_fi[0], "center_y": self.xsw_f_fi[1]} or self.ids.common10.pos_hint == {"center_x": self.xse_f_fi[0], "center_y": self.xse_f_fi[1]} or self.ids.common10.pos_hint == {"center_x": self.xne_f_fi[0], "center_y": self.xne_f_fi[1]}:
                        mid = ((self.ids.common10.pos_hint['center_x'] + pb_co[0])/2 , (self.ids.common10.pos_hint['center_y'] + pb_co[1])/2)
                        for j in range(1, 21):
                            if (self.ids[f'p1{j}'].pos_hint == {"center_x": self.w_f_fi[0], "center_y": self.w_f_fi[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.e_f_fi[0], "center_y": self.e_f_fi[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.s_f_fi[0], "center_y": self.s_f_fi[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.n_f_fi[0], "center_y": self.n_f_fi[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.sw_f_fi[0], "center_y": self.sw_f_fi[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.se_f_fi[0], "center_y": self.se_f_fi[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.nw_f_fi[0], "center_y": self.nw_f_fi[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.ne_f_fi[0], "center_y": self.ne_f_fi[1]}) and self.ids[f'p1{i}'].icon == "account":
                                if self.ids[f'p1{j}'].pos_hint == {'center_x': mid[0], 'center_y': mid[1]}:
                                    self.ids.common10.text_color = 0,0.2,0.21,0.31  
                        for j in range(1, 21):
                            if (self.ids[f'p2{j}'].pos_hint == {"center_x": self.w_f_fi[0], "center_y": self.w_f_fi[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.e_f_fi[0], "center_y": self.e_f_fi[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.s_f_fi[0], "center_y": self.s_f_fi[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.n_f_fi[0], "center_y": self.n_f_fi[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.sw_f_fi[0], "center_y": self.sw_f_fi[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.se_f_fi[0], "center_y": self.se_f_fi[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.nw_f_fi[0], "center_y": self.nw_f_fi[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.ne_f_fi[0], "center_y": self.ne_f_fi[1]}) and self.ids[f'p2{i}'].icon == "account":
                                if self.ids[f'p2{i}'].pos_hint == {'center_x': mid[0], 'center_y': mid[1]}:
                                    self.ids.common10.text_color = 245/255, 5/255, 237/255  
                    for i in range(1, 21):
                        if (self.ids[f'p2{i}'].pos_hint == {"center_x": self.xn_f_fi[0], "center_y": self.xn_f_fi[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.xw_f_fi[0], "center_y": self.xw_f_fi[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.xs_f_fi[0], "center_y": self.xs_f_fi[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.xe_f_fi[0], "center_y": self.xe_f_fi[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.xne_f_fi[0], "center_y": self.xne_f_fi[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.xnw_f_fi[0], "center_y": self.xnw_f_fi[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.xsw_f_fi[0], "center_y": self.xsw_f_fi[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.xse_f_fi[0], "center_y": self.xse_f_fi[1]}) and self.ids[f'p2{i}'].text_color == [0,0.2,0.21,0.31] and self.ids[f'p2{i}'].icon == "record-circle":
                            midp1 = ((self.ids[f'p2{i}'].pos_hint['center_x'] + pb_co[0])/2, (self.ids[f'p2{i}'].pos_hint['center_y'] + pb_co[1])/2)
                            for j in range(1, 21):
                                if (self.ids[f'p1{j}'].pos_hint == {"center_x": self.w_f_fi[0], "center_y": self.w_f_fi[1]} or self.ids[f'p1{j}'].pos_hint == {"center_x": self.e_f_fi[0], "center_y": self.e_f_fi[1]} or self.ids[f'p1{j}'].pos_hint == {"center_x": self.s_f_fi[0], "center_y": self.s_f_fi[1]} or self.ids[f'p1{j}'].pos_hint == {"center_x": self.n_f_fi[0], "center_y": self.n_f_fi[1]} or self.ids[f'p1{j}'].pos_hint == {"center_x": self.sw_f_fi[0], "center_y": self.sw_f_fi[1]} or self.ids[f'p1{j}'].pos_hint == {"center_x": self.se_f_fi[0], "center_y": self.se_f_fi[1]} or self.ids[f'p1{j}'].pos_hint == {"center_x": self.nw_f_fi[0], "center_y": self.nw_f_fi[1]} or self.ids[f'p1{j}'].pos_hint == {"center_x": self.ne_f_fi[0], "center_y": self.ne_f_fi[1]}) and self.ids[f'p1{j}'].icon == "account":
                                    if self.ids[f'p1{j}'].pos_hint == {'center_x': midp1[0], 'center_y': midp1[1]}:
                                        self.ids[f'p2{i}'].text_color = 0,0.2,0.21,0.31   
                        if (self.ids[f'p1{i}'].pos_hint == {"center_x": self.xw_f_fi[0], "center_y": self.xw_f_fi[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.xe_f_fi[0], "center_y": self.xe_f_fi[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.xs_f_fi[0], "center_y": self.xs_f_fi[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.xn_f_fi[0], "center_y": self.xn_f_fi[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.xnw_f_fi[0], "center_y": self.xnw_f_fi[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.xsw_f_fi[0], "center_y": self.xsw_f_fi[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.xse_f_fi[0], "center_y": self.xse_f_fi[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.xne_f_fi[0], "center_y": self.xne_f_fi[1]}) and self.ids[f'p1{i}'].text_color == [0,0.2,0.21,0.31] and self.ids[f'p1{i}'].icon == "record-circle":
                            midp11 = ((self.ids[f'p1{i}'].pos_hint['center_x'] + pb_co[0])/2, (self.ids[f'p1{i}'].pos_hint['center_y'] + pb_co[1])/2)
                            for j in range(1, 21):
                                if (self.ids[f'p1{j}'].pos_hint == {"center_x": self.w_f_fi[0], "center_y": self.w_f_fi[1]} or self.ids[f'p1{j}'].pos_hint == {"center_x": self.e_f_fi[0], "center_y": self.e_f_fi[1]} or self.ids[f'p1{j}'].pos_hint == {"center_x": self.s_f_fi[0], "center_y": self.s_f_fi[1]} or self.ids[f'p1{j}'].pos_hint == {"center_x": self.n_f_fi[0], "center_y": self.n_f_fi[1]} or self.ids[f'p1{j}'].pos_hint == {"center_x": self.sw_f_fi[0], "center_y": self.sw_f_fi[1]} or self.ids[f'p1{j}'].pos_hint == {"center_x": self.se_f_fi[0], "center_y": self.se_f_fi[1]} or self.ids[f'p1{j}'].pos_hint == {"center_x": self.nw_f_fi[0], "center_y": self.nw_f_fi[1]} or self.ids[f'p1{j}'].pos_hint == {"center_x": self.ne_f_fi[0], "center_y": self.ne_f_fi[1]}) and self.ids[f'p1{j}'].icon == "account":
                                    if self.ids[f'p1{j}'].pos_hint == {'center_x': midp11[0], 'center_y': midp11[1]}:
                                        self.ids[f'p1{i}'].text_color = 0,0.2,0.21,0.31   
                    for i in range(1, 21):
                        if (self.ids[f'p2{i}'].pos_hint == {"center_x": self.xn_f_fi[0], "center_y": self.xn_f_fi[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.xw_f_fi[0], "center_y": self.xw_f_fi[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.xs_f_fi[0], "center_y": self.xs_f_fi[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.xe_f_fi[0], "center_y": self.xe_f_fi[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.xne_f_fi[0], "center_y": self.xne_f_fi[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.xnw_f_fi[0], "center_y": self.xnw_f_fi[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.xsw_f_fi[0], "center_y": self.xsw_f_fi[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.xse_f_fi[0], "center_y": self.xse_f_fi[1]}) and self.ids[f'p2{i}'].text_color == [0,0.2,0.21,0.31] and self.ids[f'p2{i}'].icon == "record-circle":
                            midp1 = ((self.ids[f'p2{i}'].pos_hint['center_x'] + pb_co[0])/2, (self.ids[f'p2{i}'].pos_hint['center_y'] + pb_co[1])/2)
                            for j in range(1, 21):
                                if (self.ids[f'p2{j}'].pos_hint == {"center_x": self.w_f_fi[0], "center_y": self.w_f_fi[1]} or self.ids[f'p2{j}'].pos_hint == {"center_x": self.e_f_fi[0], "center_y": self.e_f_fi[1]} or self.ids[f'p2{j}'].pos_hint == {"center_x": self.s_f_fi[0], "center_y": self.s_f_fi[1]} or self.ids[f'p2{j}'].pos_hint == {"center_x": self.n_f_fi[0], "center_y": self.n_f_fi[1]} or self.ids[f'p2{j}'].pos_hint == {"center_x": self.sw_f_fi[0], "center_y": self.sw_f_fi[1]} or self.ids[f'p2{j}'].pos_hint == {"center_x": self.se_f_fi[0], "center_y": self.se_f_fi[1]} or self.ids[f'p2{j}'].pos_hint == {"center_x": self.nw_f_fi[0], "center_y": self.nw_f_fi[1]} or self.ids[f'p2{j}'].pos_hint == {"center_x": self.ne_f_fi[0], "center_y": self.ne_f_fi[1]}) and self.ids[f'p2{j}'].icon == "account":
                                    if self.ids[f'p2{j}'].pos_hint == {'center_x': midp1[0], 'center_y': midp1[1]}:
                                        self.ids[f'p2{i}'].text_color = 245/255, 5/255, 237/255
                        if (self.ids[f'p1{i}'].pos_hint == {"center_x": self.xw_f_fi[0], "center_y": self.xw_f_fi[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.xe_f_fi[0], "center_y": self.xe_f_fi[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.xs_f_fi[0], "center_y": self.xs_f_fi[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.xn_f_fi[0], "center_y": self.xn_f_fi[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.xnw_f_fi[0], "center_y": self.xnw_f_fi[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.xsw_f_fi[0], "center_y": self.xsw_f_fi[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.xse_f_fi[0], "center_y": self.xse_f_fi[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.xne_f_fi[0], "center_y": self.xne_f_fi[1]}) and self.ids[f'p1{i}'].text_color == [0,0.2,0.21,0.31] and self.ids[f'p1{i}'].icon == "record-circle":
                            midp11 = ((self.ids[f'p1{i}'].pos_hint['center_x'] + pb_co[0])/2, (self.ids[f'p1{i}'].pos_hint['center_y'] + pb_co[1])/2)
                            for j in range(1, 21):
                                if (self.ids[f'p2{j}'].pos_hint == {"center_x": self.w_f_fi[0], "center_y": self.w_f_fi[1]} or self.ids[f'p2{j}'].pos_hint == {"center_x": self.e_f_fi[0], "center_y": self.e_f_fi[1]} or self.ids[f'p2{j}'].pos_hint == {"center_x": self.s_f_fi[0], "center_y": self.s_f_fi[1]} or self.ids[f'p2{j}'].pos_hint == {"center_x": self.n_f_fi[0], "center_y": self.n_f_fi[1]} or self.ids[f'p2{j}'].pos_hint == {"center_x": self.sw_f_fi[0], "center_y": self.sw_f_fi[1]} or self.ids[f'p2{j}'].pos_hint == {"center_x": self.se_f_fi[0], "center_y": self.se_f_fi[1]} or self.ids[f'p2{j}'].pos_hint == {"center_x": self.nw_f_fi[0], "center_y": self.nw_f_fi[1]} or self.ids[f'p2{j}'].pos_hint == {"center_x": self.ne_f_fi[0], "center_y": self.ne_f_fi[1]}) and self.ids[f'p2{j}'].icon == "account":
                                    if self.ids[f'p2{j}'].pos_hint == {'center_x': midp11[0], 'center_y': midp11[1]}:
                                        self.ids[f'p1{i}'].text_color = 245/255, 5/255, 237/255  

        elif pb_co == (0,3*y) or pb_co == (2*x, 3*y) or pb_co == (4*x, 3*y) or pb_co == (x,4*y) or pb_co == (3*x,4*y) or pb_co == (0,5*y) or pb_co == (2*x,5*y) or pb_co==(4*x,5*y) or pb_co == (2*x, y) or pb_co == (x,0) or pb_co == (3*x, 0) or pb_co == (x,8*y) or pb_co == (3*x, 8*y) or pb_co==(2*x, 7*y):
            self.w_f_fi = (pb_co[0] - x, pb_co[1])
            self.e_f_fi = (pb_co[0]+x, pb_co[1])
            self.n_f_fi = (pb_co[0], pb_co[1]+y)
            self.s_f_fi = (pb_co[0], pb_co[1]-y)
            self.xw_f_fi = (pb_co[0] - 2*x, pb_co[1])
            self.xe_f_fi = (pb_co[0]+2*x, pb_co[1])
            self.xn_f_fi = (pb_co[0], pb_co[1]+2*y)
            self.xs_f_fi = (pb_co[0], pb_co[1]-2*y)
            if self.ids.common10.pos_hint == {"center_x": self.w_f_fi[0], "center_y": self.w_f_fi[1]} or self.ids.common10.pos_hint == {"center_x": self.e_f_fi[0], "center_y": self.e_f_fi[1]} or self.ids.common10.pos_hint == {"center_x": self.s_f_fi[0], "center_y": self.s_f_fi[1]} or self.ids.common10.pos_hint == {"center_x": self.n_f_fi[0], "center_y": self.n_f_fi[1]}:
                self.ids.common10.text_color = 245/255, 5/255, 237/255
            for i in range(1, 21):
                if (self.ids[f'p2{i}'].pos_hint == {"center_x": self.w_f_fi[0], "center_y": self.w_f_fi[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.e_f_fi[0], "center_y": self.e_f_fi[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.s_f_fi[0], "center_y": self.s_f_fi[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.n_f_fi[0], "center_y": self.n_f_fi[1]}) and self.ids[f'p2{i}'].text_color == [0,0.2,0.21,0.31] and self.ids[f'p2{i}'].icon == "record-circle":
                    self.ids[f'p2{i}'].text_color = 245/255, 5/255, 237/255                
                if (self.ids[f'p1{i}'].pos_hint == {"center_x": self.w_f_fi[0], "center_y": self.w_f_fi[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.e_f_fi[0], "center_y": self.e_f_fi[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.s_f_fi[0], "center_y": self.s_f_fi[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.n_f_fi[0], "center_y": self.n_f_fi[1]}) and self.ids[f'p1{i}'].text_color == [0,0.2,0.21,0.31] and self.ids[f'p1{i}'].icon == "record-circle":
                    self.ids[f'p1{i}'].text_color = 245/255, 5/255, 237/255
            for i in range(1, 21):
                if (self.ids[f'p2{i}'].pos_hint == {"center_x": self.w_f_fi[0], "center_y": self.w_f_fi[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.e_f_fi[0], "center_y": self.e_f_fi[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.s_f_fi[0], "center_y": self.s_f_fi[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.n_f_fi[0], "center_y": self.n_f_fi[1]}) and self.ids[f'p2{i}'].icon != "record-circle":
                    if self.ids.common10.pos_hint == {"center_x": self.xw_f_fi[0], "center_y": self.xw_f_fi[1]} or self.ids.common10.pos_hint == {"center_x": self.xe_f_fi[0], "center_y": self.xe_f_fi[1]} or self.ids.common10.pos_hint == {"center_x": self.xs_f_fi[0], "center_y": self.xs_f_fi[1]} or self.ids.common10.pos_hint == {"center_x": self.xn_f_fi[0], "center_y": self.xn_f_fi[1]}:
                        mid = ((self.ids.common10.pos_hint['center_x'] + pb_co[0])/2 , (self.ids.common10.pos_hint['center_y'] + pb_co[1])/2)
                        for j in range(1, 21):
                            if (self.ids[f'p1{j}'].pos_hint == {"center_x": self.w_f_fi[0], "center_y": self.w_f_fi[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.e_f_fi[0], "center_y": self.e_f_fi[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.s_f_fi[0], "center_y": self.s_f_fi[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.n_f_fi[0], "center_y": self.n_f_fi[1]}) and self.ids[f'p1{i}'].icon == "account":
                                if self.ids[f'p1{j}'].pos_hint == {'center_x': mid[0], 'center_y': mid[1]}:
                                    self.ids.common10.text_color = 0,0.2,0.21,0.31  
                        for j in range(1, 21):
                            if (self.ids[f'p2{j}'].pos_hint == {"center_x": self.w_f_fi[0], "center_y": self.w_f_fi[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.e_f_fi[0], "center_y": self.e_f_fi[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.s_f_fi[0], "center_y": self.s_f_fi[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.n_f_fi[0], "center_y": self.n_f_fi[1]}) and self.ids[f'p2{i}'].icon == "account":
                                if self.ids[f'p2{j}'].pos_hint == {'center_x': mid[0], 'center_y': mid[1]}:
                                    self.ids.common10.text_color = 245/255, 5/255, 237/255
                          
                    for i in range(1, 21):
                        if (self.ids[f'p2{i}'].pos_hint == {"center_x": self.xn_f_fi[0], "center_y": self.xn_f_fi[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.xw_f_fi[0], "center_y": self.xw_f_fi[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.xs_f_fi[0], "center_y": self.xs_f_fi[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.xe_f_fi[0], "center_y": self.xe_f_fi[1]}) and self.ids[f'p2{i}'].text_color == [0,0.2,0.21,0.31] and self.ids[f'p2{i}'].icon == "record-circle":
                            midp1 = ((self.ids[f'p2{i}'].pos_hint['center_x'] + pb_co[0])/2, (self.ids[f'p2{i}'].pos_hint['center_y'] + pb_co[1])/2)
                            for j in range(1, 21):
                                if (self.ids[f'p1{j}'].pos_hint == {"center_x": self.w_f_fi[0], "center_y": self.w_f_fi[1]} or self.ids[f'p1{j}'].pos_hint == {"center_x": self.e_f_fi[0], "center_y": self.e_f_fi[1]} or self.ids[f'p1{j}'].pos_hint == {"center_x": self.s_f_fi[0], "center_y": self.s_f_fi[1]} or self.ids[f'p1{j}'].pos_hint == {"center_x": self.n_f_fi[0], "center_y": self.n_f_fi[1]}) and self.ids[f'p1{j}'].icon == "account":
                                    if self.ids[f'p1{j}'].pos_hint == {'center_x': midp1[0], 'center_y': midp1[1]}:
                                        self.ids[f'p2{i}'].text_color = 0,0.2,0.21,0.31  
                        if (self.ids[f'p1{i}'].pos_hint == {"center_x": self.xw_f_fi[0], "center_y": self.xw_f_fi[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.xe_f_fi[0], "center_y": self.xe_f_fi[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.xs_f_fi[0], "center_y": self.xs_f_fi[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.xn_f_fi[0], "center_y": self.xn_f_fi[1]}) and self.ids[f'p1{i}'].text_color == [0,0.2,0.21,0.31] and self.ids[f'p1{i}'].icon == "record-circle":
                            midp11 = ((self.ids[f'p1{i}'].pos_hint['center_x'] + pb_co[0])/2, (self.ids[f'p1{i}'].pos_hint['center_y'] + pb_co[1])/2)
                            for j in range(1, 21):
                                if (self.ids[f'p1{j}'].pos_hint == {"center_x": self.w_f_fi[0], "center_y": self.w_f_fi[1]} or self.ids[f'p1{j}'].pos_hint == {"center_x": self.e_f_fi[0], "center_y": self.e_f_fi[1]} or self.ids[f'p1{j}'].pos_hint == {"center_x": self.s_f_fi[0], "center_y": self.s_f_fi[1]} or self.ids[f'p1{j}'].pos_hint == {"center_x": self.n_f_fi[0], "center_y": self.n_f_fi[1]}) and self.ids[f'p1{j}'].icon == "account":
                                    if self.ids[f'p1{j}'].pos_hint == {'center_x': midp11[0], 'center_y': midp11[1]}:
                                        self.ids[f'p1{i}'].text_color = 0,0.2,0.21,0.31  
                    for i in range(1, 21):
                        if (self.ids[f'p2{i}'].pos_hint == {"center_x": self.xn_f_fi[0], "center_y": self.xn_f_fi[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.xw_f_fi[0], "center_y": self.xw_f_fi[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.xs_f_fi[0], "center_y": self.xs_f_fi[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.xe_f_fi[0], "center_y": self.xe_f_fi[1]}) and self.ids[f'p2{i}'].text_color == [0,0.2,0.21,0.31] and self.ids[f'p2{i}'].icon == "record-circle":
                            midp1 = ((self.ids[f'p2{i}'].pos_hint['center_x'] + pb_co[0])/2, (self.ids[f'p2{i}'].pos_hint['center_y'] + pb_co[1])/2)
                            for j in range(1, 21):
                                if (self.ids[f'p2{j}'].pos_hint == {"center_x": self.w_f_fi[0], "center_y": self.w_f_fi[1]} or self.ids[f'p2{j}'].pos_hint == {"center_x": self.e_f_fi[0], "center_y": self.e_f_fi[1]} or self.ids[f'p2{j}'].pos_hint == {"center_x": self.s_f_fi[0], "center_y": self.s_f_fi[1]} or self.ids[f'p2{j}'].pos_hint == {"center_x": self.n_f_fi[0], "center_y": self.n_f_fi[1]}) and self.ids[f'p2{j}'].icon == "account":
                                    if self.ids[f'p2{j}'].pos_hint == {'center_x': midp1[0], 'center_y': midp1[1]}:
                                        self.ids[f'p2{i}'].text_color = 245/255, 5/255, 237/255  
                        if (self.ids[f'p1{i}'].pos_hint == {"center_x": self.xw_f_fi[0], "center_y": self.xw_f_fi[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.xe_f_fi[0], "center_y": self.xe_f_fi[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.xs_f_fi[0], "center_y": self.xs_f_fi[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.xn_f_fi[0], "center_y": self.xn_f_fi[1]}) and self.ids[f'p1{i}'].text_color == [0,0.2,0.21,0.31] and self.ids[f'p1{i}'].icon == "record-circle":
                            midp11 = ((self.ids[f'p1{i}'].pos_hint['center_x'] + pb_co[0])/2, (self.ids[f'p1{i}'].pos_hint['center_y'] + pb_co[1])/2)
                            for j in range(1, 21):
                                if (self.ids[f'p2{j}'].pos_hint == {"center_x": self.w_f_fi[0], "center_y": self.w_f_fi[1]} or self.ids[f'p2{j}'].pos_hint == {"center_x": self.e_f_fi[0], "center_y": self.e_f_fi[1]} or self.ids[f'p2{j}'].pos_hint == {"center_x": self.s_f_fi[0], "center_y": self.s_f_fi[1]} or self.ids[f'p2{j}'].pos_hint == {"center_x": self.n_f_fi[0], "center_y": self.n_f_fi[1]}) and self.ids[f'p2{j}'].icon == "account":
                                    if self.ids[f'p2{j}'].pos_hint == {'center_x': midp11[0], 'center_y': midp11[1]}:
                                        self.ids[f'p1{i}'].text_color = 245/255, 5/255, 237/255
        elif pb_co == (x,2*y) or pb_co == (3*x, 2*y):
            self.w_f_se = (pb_co[0] - x, pb_co[1])
            self.e_f_se = (pb_co[0]+x, pb_co[1])
            self.n_f_se = (pb_co[0], pb_co[1]+y)
            self.s_f_se = (pb_co[0], pb_co[1]-y)
            self.xw_f_se = (pb_co[0] - 2*x, pb_co[1])
            self.xe_f_se = (pb_co[0]+2*x, pb_co[1])
            self.xn_f_se = (pb_co[0], pb_co[1]+2*y)
            self.xs_f_se = (pb_co[0], pb_co[1]-2*y)
            if self.ids.common10.pos_hint == {"center_x": self.w_f_se[0], "center_y": self.w_f_se[1]} or self.ids.common10.pos_hint == {"center_x": self.e_f_se[0], "center_y": self.e_f_se[1]} or self.ids.common10.pos_hint == {"center_x": self.n_f_se[0], "center_y": self.n_f_se[1]}:
                self.ids.common10.text_color = 245/255, 5/255, 237/255
            for i in range(1, 21):
                if (self.ids[f'p1{i}'].pos_hint == {"center_x": self.w_f_se[0], "center_y": self.w_f_se[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.e_f_se[0], "center_y": self.e_f_se[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.n_f_se[0], "center_y": self.n_f_se[1]}) and self.ids[f'p1{i}'].text_color == [0,0.2,0.21,0.31] and self.ids[f'p1{i}'].icon == "record-circle":
                    self.ids[f'p1{i}'].text_color = 245/255, 5/255, 237/255                
                if (self.ids[f'p2{i}'].pos_hint == {"center_x": self.w_f_se[0], "center_y": self.w_f_se[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.e_f_se[0], "center_y": self.e_f_se[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.n_f_se[0], "center_y": self.n_f_se[1]}) and self.ids[f'p2{i}'].text_color == [0,0.2,0.21,0.31] and self.ids[f'p2{i}'].icon == "record-circle":
                    self.ids[f'p2{i}'].text_color = 245/255, 5/255, 237/255
            for i in range(1, 21):
                if (self.ids[f'p2{i}'].pos_hint == {"center_x": self.w_f_se[0], "center_y": self.w_f_se[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.e_f_se[0], "center_y": self.e_f_se[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.n_f_se[0], "center_y": self.n_f_se[1]}) and self.ids[f'p2{i}'].icon != "record-circle":
                    if self.ids.common10.pos_hint == {"center_x": self.xw_f_se[0], "center_y": self.xw_f_se[1]} or self.ids.common10.pos_hint == {"center_x": self.xe_f_se[0], "center_y": self.xe_f_se[1]} or self.ids.common10.pos_hint == {"center_x": self.xn_f_se[0], "center_y": self.xn_f_se[1]}:
                        mid = ((self.ids.common10.pos_hint['center_x'] + pb_co[0])/2 , (self.ids.common10.pos_hint['center_y'] + pb_co[1])/2)
                        for j in range(1, 21):
                            if (self.ids[f'p1{j}'].pos_hint == {"center_x": self.w_f_se[0], "center_y": self.w_f_se[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.e_f_se[0], "center_y": self.e_f_se[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.n_f_se[0], "center_y": self.n_f_se[1]}) and self.ids[f'p1{i}'].icon == "account":
                                if self.ids[f'p1{j}'].pos_hint == {'center_x': mid[0], 'center_y': mid[1]}:
                                    self.ids.common10.text_color = 0,0.2,0.21,0.31  
                        for j in range(1, 21):
                            if (self.ids[f'p2{j}'].pos_hint == {"center_x": self.w_f_se[0], "center_y": self.w_f_se[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.e_f_se[0], "center_y": self.e_f_se[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.n_f_se[0], "center_y": self.n_f_se[1]}) and self.ids[f'p2{i}'].icon == "account":
                                if self.ids[f'p2{j}'].pos_hint == {'center_x': mid[0], 'center_y': mid[1]}:
                                    self.ids.common10.text_color = 245/255, 5/255, 237/255
                          
                    for i in range(1, 21):
                        if (self.ids[f'p2{i}'].pos_hint == {"center_x": self.xn_f_se[0], "center_y": self.xn_f_se[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.xw_f_se[0], "center_y": self.xw_f_se[1]}  or self.ids[f'p2{i}'].pos_hint == {"center_x": self.xe_f_se[0], "center_y": self.xe_f_se[1]}) and self.ids[f'p2{i}'].text_color == [0,0.2,0.21,0.31] and self.ids[f'p2{i}'].icon == "record-circle":
                            midp1 = ((self.ids[f'p2{i}'].pos_hint['center_x'] + pb_co[0])/2, (self.ids[f'p2{i}'].pos_hint['center_y'] + pb_co[1])/2)
                            for j in range(1, 21):
                                if (self.ids[f'p1{j}'].pos_hint == {"center_x": self.w_f_se[0], "center_y": self.w_f_se[1]} or self.ids[f'p1{j}'].pos_hint == {"center_x": self.e_f_se[0], "center_y": self.e_f_se[1]}  or self.ids[f'p1{j}'].pos_hint == {"center_x": self.n_f_se[0], "center_y": self.n_f_se[1]}) and self.ids[f'p1{j}'].icon == "account":
                                    if self.ids[f'p1{j}'].pos_hint == {'center_x': midp1[0], 'center_y': midp1[1]}:
                                        self.ids[f'p2{i}'].text_color = 0,0.2,0.21,0.31  
                        if (self.ids[f'p1{i}'].pos_hint == {"center_x": self.xw_f_se[0], "center_y": self.xw_f_se[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.xe_f_se[0], "center_y": self.xe_f_se[1]}  or self.ids[f'p1{i}'].pos_hint == {"center_x": self.xn_f_se[0], "center_y": self.xn_f_se[1]}) and self.ids[f'p1{i}'].text_color == [0,0.2,0.21,0.31] and self.ids[f'p1{i}'].icon == "record-circle":
                            midp11 = ((self.ids[f'p1{i}'].pos_hint['center_x'] + pb_co[0])/2, (self.ids[f'p1{i}'].pos_hint['center_y'] + pb_co[1])/2)
                            for j in range(1, 21):
                                if (self.ids[f'p1{j}'].pos_hint == {"center_x": self.w_f_se[0], "center_y": self.w_f_se[1]} or self.ids[f'p1{j}'].pos_hint == {"center_x": self.e_f_se[0], "center_y": self.e_f_se[1]}  or self.ids[f'p1{j}'].pos_hint == {"center_x": self.n_f_se[0], "center_y": self.n_f_se[1]}) and self.ids[f'p1{j}'].icon == "account":
                                    if self.ids[f'p1{j}'].pos_hint == {'center_x': midp11[0], 'center_y': midp11[1]}:
                                        self.ids[f'p1{i}'].text_color = 0,0.2,0.21,0.31  
                    for i in range(1, 21):
                        if (self.ids[f'p2{i}'].pos_hint == {"center_x": self.xn_f_se[0], "center_y": self.xn_f_se[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.xw_f_se[0], "center_y": self.xw_f_se[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.xe_f_se[0], "center_y": self.xe_f_se[1]}) and self.ids[f'p2{i}'].text_color == [0,0.2,0.21,0.31] and self.ids[f'p2{i}'].icon == "record-circle":
                            midp1 = ((self.ids[f'p2{i}'].pos_hint['center_x'] + pb_co[0])/2, (self.ids[f'p2{i}'].pos_hint['center_y'] + pb_co[1])/2)
                            for j in range(1, 21):
                                if (self.ids[f'p2{j}'].pos_hint == {"center_x": self.w_f_se[0], "center_y": self.w_f_se[1]} or self.ids[f'p2{j}'].pos_hint == {"center_x": self.e_f_se[0], "center_y": self.e_f_se[1]}  or self.ids[f'p2{j}'].pos_hint == {"center_x": self.n_f_se[0], "center_y": self.n_f_se[1]}) and self.ids[f'p2{j}'].icon == "account":
                                    if self.ids[f'p2{j}'].pos_hint == {'center_x': midp1[0], 'center_y': midp1[1]}:
                                        self.ids[f'p2{i}'].text_color = 245/255, 5/255, 237/255  
                        if (self.ids[f'p1{i}'].pos_hint == {"center_x": self.xw_f_se[0], "center_y": self.xw_f_se[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.xe_f_se[0], "center_y": self.xe_f_se[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.xn_f_se[0], "center_y": self.xn_f_se[1]}) and self.ids[f'p1{i}'].text_color == [0,0.2,0.21,0.31] and self.ids[f'p1{i}'].icon == "record-circle":
                            midp11 = ((self.ids[f'p1{i}'].pos_hint['center_x'] + pb_co[0])/2, (self.ids[f'p1{i}'].pos_hint['center_y'] + pb_co[1])/2)
                            for j in range(1, 21):
                                if (self.ids[f'p2{j}'].pos_hint == {"center_x": self.w_f_se[0], "center_y": self.w_f_se[1]} or self.ids[f'p2{j}'].pos_hint == {"center_x": self.e_f_se[0], "center_y": self.e_f_se[1]}  or self.ids[f'p2{j}'].pos_hint == {"center_x": self.n_f_se[0], "center_y": self.n_f_se[1]}) and self.ids[f'p2{j}'].icon == "account":
                                    if self.ids[f'p2{j}'].pos_hint == {'center_x': midp11[0], 'center_y': midp11[1]}:
                                        self.ids[f'p1{i}'].text_color = 245/255, 5/255, 237/255
        elif pb_co == (x,6*y) or pb_co == (3*x, 6*y):
            self.w_f_fi = (pb_co[0] - x, pb_co[1])
            self.e_f_fi = (pb_co[0]+x, pb_co[1])
            self.s_f_fi = (pb_co[0], pb_co[1]-y)
            self.xw_f_fi = (pb_co[0] - 2*x, pb_co[1])
            self.xe_f_fi = (pb_co[0]+2*x, pb_co[1])
            self.xs_f_fi = (pb_co[0], pb_co[1]-2*y)
            if self.ids.common10.pos_hint == {"center_x": self.w_f_fi[0], "center_y": self.w_f_fi[1]} or self.ids.common10.pos_hint == {"center_x": self.e_f_fi[0], "center_y": self.e_f_fi[1]} or self.ids.common10.pos_hint == {"center_x": self.s_f_fi[0], "center_y": self.s_f_fi[1]}:
                self.ids.common10.text_color = 245/255, 5/255, 237/255
            for i in range(1, 21):
                if (self.ids[f'p2{i}'].pos_hint == {"center_x": self.w_f_fi[0], "center_y": self.w_f_fi[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.e_f_fi[0], "center_y": self.e_f_fi[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.s_f_fi[0], "center_y": self.s_f_fi[1]}) and self.ids[f'p2{i}'].text_color == [0,0.2,0.21,0.31] and self.ids[f'p2{i}'].icon == "record-circle":
                    self.ids[f'p2{i}'].text_color = 245/255, 5/255, 237/255                
                if (self.ids[f'p1{i}'].pos_hint == {"center_x": self.w_f_fi[0], "center_y": self.w_f_fi[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.e_f_fi[0], "center_y": self.e_f_fi[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.s_f_fi[0], "center_y": self.s_f_fi[1]}) and self.ids[f'p1{i}'].text_color == [0,0.2,0.21,0.31] and self.ids[f'p1{i}'].icon == "record-circle":
                    self.ids[f'p1{i}'].text_color = 245/255, 5/255, 237/255
            for i in range(1, 21):
                if (self.ids[f'p2{i}'].pos_hint == {"center_x": self.w_f_fi[0], "center_y": self.w_f_fi[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.e_f_fi[0], "center_y": self.e_f_fi[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.s_f_fi[0], "center_y": self.s_f_fi[1]}) and self.ids[f'p2{i}'].icon != "record-circle":
                    if self.ids.common10.pos_hint == {"center_x": self.xw_f_fi[0], "center_y": self.xw_f_fi[1]} or self.ids.common10.pos_hint == {"center_x": self.xe_f_fi[0], "center_y": self.xe_f_fi[1]} or self.ids.common10.pos_hint == {"center_x": self.xs_f_fi[0], "center_y": self.xs_f_fi[1]}:
                        mid = ((self.ids.common10.pos_hint['center_x'] + pb_co[0])/2 , (self.ids.common10.pos_hint['center_y'] + pb_co[1])/2)
                        for j in range(1, 21):
                            if (self.ids[f'p1{j}'].pos_hint == {"center_x": self.w_f_fi[0], "center_y": self.w_f_fi[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.e_f_fi[0], "center_y": self.e_f_fi[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.s_f_fi[0], "center_y": self.s_f_fi[1]}) and self.ids[f'p1{i}'].icon == "account":
                                if self.ids[f'p1{i}'].pos_hint == {'center_x': mid[0], 'center_y': mid[1]}:
                                    self.ids.common10.text_color = 0,0.2,0.21,0.31  
                        for j in range(1, 21):
                            if (self.ids[f'p2{j}'].pos_hint == {"center_x": self.w_f_fi[0], "center_y": self.w_f_fi[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.e_f_fi[0], "center_y": self.e_f_fi[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.s_f_fi[0], "center_y": self.s_f_fi[1]}) and self.ids[f'p2{i}'].icon == "account":
                                if self.ids[f'p2{i}'].pos_hint == {'center_x': mid[0], 'center_y': mid[1]}:
                                    self.ids.common10.text_color = 245/255, 5/255, 237/255
                          
                    for i in range(1, 21):
                        if (self.ids[f'p2{i}'].pos_hint == {"center_x": self.xs_f_fi[0], "center_y": self.xs_f_fi[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.xw_f_fi[0], "center_y": self.xw_f_fi[1]}  or self.ids[f'p2{i}'].pos_hint == {"center_x": self.xe_f_fi[0], "center_y": self.xe_f_fi[1]}) and self.ids[f'p2{i}'].text_color == [0,0.2,0.21,0.31] and self.ids[f'p2{i}'].icon == "record-circle":
                            midp1 = ((self.ids[f'p2{i}'].pos_hint['center_x'] + pb_co[0])/2, (self.ids[f'p2{i}'].pos_hint['center_y'] + pb_co[1])/2)
                            for j in range(1, 21):
                                if (self.ids[f'p1{j}'].pos_hint == {"center_x": self.w_f_fi[0], "center_y": self.w_f_fi[1]} or self.ids[f'p1{j}'].pos_hint == {"center_x": self.e_f_fi[0], "center_y": self.e_f_fi[1]}  or self.ids[f'p1{j}'].pos_hint == {"center_x": self.s_f_fi[0], "center_y": self.s_f_fi[1]}) and self.ids[f'p1{j}'].icon == "account":
                                    if self.ids[f'p1{j}'].pos_hint == {'center_x': midp1[0], 'center_y': midp1[1]}:
                                        self.ids[f'p2{i}'].text_color = 0,0.2,0.21,0.31  
                        if (self.ids[f'p1{i}'].pos_hint == {"center_x": self.xw_f_fi[0], "center_y": self.xw_f_fi[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.xe_f_fi[0], "center_y": self.xe_f_fi[1]}  or self.ids[f'p1{i}'].pos_hint == {"center_x": self.xs_f_fi[0], "center_y": self.xs_f_fi[1]}) and self.ids[f'p1{i}'].text_color == [0,0.2,0.21,0.31] and self.ids[f'p1{i}'].icon == "record-circle":
                            midp11 = ((self.ids[f'p1{i}'].pos_hint['center_x'] + pb_co[0])/2, (self.ids[f'p1{i}'].pos_hint['center_y'] + pb_co[1])/2)
                            for j in range(1, 21):
                                if (self.ids[f'p1{j}'].pos_hint == {"center_x": self.w_f_fi[0], "center_y": self.w_f_fi[1]} or self.ids[f'p1{j}'].pos_hint == {"center_x": self.e_f_fi[0], "center_y": self.e_f_fi[1]}  or self.ids[f'p1{j}'].pos_hint == {"center_x": self.s_f_fi[0], "center_y": self.s_f_fi[1]}) and self.ids[f'p1{j}'].icon == "account":
                                    if self.ids[f'p1{j}'].pos_hint == {'center_x': midp11[0], 'center_y': midp11[1]}:
                                        self.ids[f'p1{i}'].text_color = 0,0.2,0.21,0.31  
                    for i in range(1, 21):
                        if (self.ids[f'p2{i}'].pos_hint == {"center_x": self.xs_f_fi[0], "center_y": self.xs_f_fi[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.xw_f_fi[0], "center_y": self.xw_f_fi[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.xe_f_fi[0], "center_y": self.xe_f_fi[1]}) and self.ids[f'p2{i}'].text_color == [0,0.2,0.21,0.31] and self.ids[f'p2{i}'].icon == "record-circle":
                            midp1 = ((self.ids[f'p2{i}'].pos_hint['center_x'] + pb_co[0])/2, (self.ids[f'p2{i}'].pos_hint['center_y'] + pb_co[1])/2)
                            for j in range(1, 21):
                                if (self.ids[f'p2{j}'].pos_hint == {"center_x": self.w_f_fi[0], "center_y": self.w_f_fi[1]} or self.ids[f'p2{j}'].pos_hint == {"center_x": self.e_f_fi[0], "center_y": self.e_f_fi[1]}  or self.ids[f'p2{j}'].pos_hint == {"center_x": self.s_f_fi[0], "center_y": self.s_f_fi[1]}) and self.ids[f'p2{j}'].icon == "account":
                                    if self.ids[f'p2{j}'].pos_hint == {'center_x': midp1[0], 'center_y': midp1[1]}:
                                        self.ids[f'p2{i}'].text_color = 245/255, 5/255, 237/255  
                        if (self.ids[f'p1{i}'].pos_hint == {"center_x": self.xw_f_fi[0], "center_y": self.xw_f_fi[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.xe_f_fi[0], "center_y": self.xe_f_fi[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.xs_f_fi[0], "center_y": self.xs_f_fi[1]}) and self.ids[f'p1{i}'].text_color == [0,0.2,0.21,0.31] and self.ids[f'p1{i}'].icon == "record-circle":
                            midp11 = ((self.ids[f'p1{i}'].pos_hint['center_x'] + pb_co[0])/2, (self.ids[f'p1{i}'].pos_hint['center_y'] + pb_co[1])/2)
                            for j in range(1, 21):
                                if (self.ids[f'p2{j}'].pos_hint == {"center_x": self.w_f_fi[0], "center_y": self.w_f_fi[1]} or self.ids[f'p2{j}'].pos_hint == {"center_x": self.e_f_fi[0], "center_y": self.e_f_fi[1]}  or self.ids[f'p2{j}'].pos_hint == {"center_x": self.s_f_fi[0], "center_y": self.s_f_fi[1]}) and self.ids[f'p2{j}'].icon == "account":
                                    if self.ids[f'p2{j}'].pos_hint == {'center_x': midp11[0], 'center_y': midp11[1]}:
                                        self.ids[f'p1{i}'].text_color = 245/255, 5/255, 237/255
        elif pb_co == (x,y):
            self.e_f_fi = (pb_co[0]+x, pb_co[1])
            self.s_f_fi = (pb_co[0], pb_co[1]-y)
            self.ne_f_fi = (pb_co[0] + x, pb_co[1] + y)
            self.sw_f_fi = (pb_co[0] - x, pb_co[1] - y)
            self.se_f_fi = (pb_co[0] + x, pb_co[1] - y)
            self.xe_f_fi = (pb_co[0]+ 2*x, pb_co[1])
            self.xne_f_fi = (pb_co[0] + 2*x, pb_co[1] + 2*y)
            if self.ids.common10.pos_hint == {"center_x": self.e_f_fi[0], "center_y": self.e_f_fi[1]} or self.ids.common10.pos_hint == {"center_x": self.s_f_fi[0], "center_y": self.s_f_fi[1]}or  self.ids.common10.pos_hint == {"center_x": self.sw_f_fi[0], "center_y": self.sw_f_fi[1]} or self.ids.common10.pos_hint == {"center_x": self.se_f_fi[0], "center_y": self.se_f_fi[1]}  or self.ids.common10.pos_hint == {"center_x": self.ne_f_fi[0], "center_y": self.ne_f_fi[1]}:
                self.ids.common10.text_color = 245/255, 5/255, 237/255
            for i in range(1, 21):
                if (self.ids[f'p2{i}'].pos_hint == {"center_x": self.e_f_fi[0], "center_y": self.e_f_fi[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.s_f_fi[0], "center_y": self.s_f_fi[1]}  or self.ids[f'p2{i}'].pos_hint == {"center_x": self.sw_f_fi[0], "center_y": self.sw_f_fi[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.se_f_fi[0], "center_y": self.se_f_fi[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.ne_f_fi[0], "center_y": self.ne_f_fi[1]}) and self.ids[f'p2{i}'].icon == "record-circle" and self.ids[f'p2{i}'].text_color == [0,0.2,0.21,0.31]:
                    self.ids[f'p2{i}'].text_color = 245/255, 5/255, 237/255
                if (self.ids[f'p1{i}'].pos_hint == {"center_x": self.e_f_fi[0], "center_y": self.e_f_fi[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.s_f_fi[0], "center_y": self.s_f_fi[1]}  or self.ids[f'p1{i}'].pos_hint == {"center_x": self.sw_f_fi[0], "center_y": self.sw_f_fi[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.se_f_fi[0], "center_y": self.se_f_fi[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.ne_f_fi[0], "center_y": self.ne_f_fi[1]}) and self.ids[f'p1{i}'].icon == "record-circle" and self.ids[f'p1{i}'].text_color == [0,0.2,0.21,0.31]:
                    self.ids[f'p1{i}'].text_color = 245/255, 5/255, 237/255
            for i in range(1, 21):
                if (self.ids[f'p2{i}'].pos_hint == {"center_x": self.e_f_fi[0], "center_y": self.e_f_fi[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.ne_f_fi[0], "center_y": self.ne_f_fi[1]}) and self.ids[f'p2{i}'].icon != "record-circle":
                    if self.ids.common10.pos_hint == {"center_x": self.xe_f_fi[0], "center_y": self.xe_f_fi[1]} or self.ids.common10.pos_hint == {"center_x": self.xne_f_fi[0], "center_y": self.xne_f_fi[1]}:
                        mid = ((self.ids.common10.pos_hint['center_x'] + pb_co[0])/2 , (self.ids.common10.pos_hint['center_y'] + pb_co[1])/2)
                        for j in range(1, 21):
                            if (self.ids[f'p1{j}'].pos_hint == {"center_x": self.e_f_fi[0], "center_y": self.e_f_fi[1]} or self.ids[f'p1{j}'].pos_hint == {"center_x": self.ne_f_fi[0], "center_y": self.ne_f_fi[1]}) and self.ids[f'p1{j}'].icon == "account":
                                if self.ids[f'p1{i}'].pos_hint == {'center_x': mid[0], 'center_y': mid[1]}:
                                    self.ids.common10.text_color = 0,0.2,0.21,0.31  
                        for j in range(1, 21):
                            if (self.ids[f'p2{j}'].pos_hint == {"center_x": self.e_f_fi[0], "center_y": self.e_f_fi[1]} or self.ids[f'p2{j}'].pos_hint == {"center_x": self.ne_f_fi[0], "center_y": self.ne_f_fi[1]}) and self.ids[f'p1{j}'].icon == "account":
                                if self.ids[f'p2{i}'].pos_hint == {'center_x': mid[0], 'center_y': mid[1]}:
                                    self.ids.common10.text_color = 245/255, 5/255, 237/255 
                    for i in range(1, 21):
                        if (self.ids[f'p2{i}'].pos_hint == {"center_x": self.xe_f_fi[0], "center_y": self.xe_f_fi[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.xne_f_fi[0], "center_y": self.xne_f_fi[1]}) and self.ids[f'p2{i}'].text_color == [0,0.2,0.21,0.31] and self.ids[f'p2{i}'].icon == "record-circle":
                            midp1 = ((self.ids[f'p2{i}'].pos_hint['center_x'] + pb_co[0])/2, (self.ids[f'p2{i}'].pos_hint['center_y'] + pb_co[1])/2)
                            for j in range(1, 21):
                                if (self.ids[f'p1{j}'].pos_hint == {"center_x": self.e_f_fi[0], "center_y": self.e_f_fi[1]} or self.ids[f'p1{j}'].pos_hint == {"center_x": self.ne_f_fi[0], "center_y": self.ne_f_fi[1]}) and self.ids[f'p1{j}'].icon == "account":
                                    if self.ids[f'p1{j}'].pos_hint == {'center_x': midp1[0], 'center_y': midp1[1]}:
                                        self.ids[f'p2{i}'].text_color = 0,0.2,0.21,0.31   
                        if (self.ids[f'p1{i}'].pos_hint == {"center_x": self.xe_f_fi[0], "center_y": self.xe_f_fi[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.xne_f_fi[0], "center_y": self.xne_f_fi[1]}) and self.ids[f'p1{i}'].text_color == [0,0.2,0.21,0.31] and self.ids[f'p1{i}'].icon == "record-circle":
                            midp11 = ((self.ids[f'p1{i}'].pos_hint['center_x'] + pb_co[0])/2, (self.ids[f'p1{i}'].pos_hint['center_y'] + pb_co[1])/2)
                            for j in range(1, 21):
                                if (self.ids[f'p1{j}'].pos_hint == {"center_x": self.e_f_fi[0], "center_y": self.e_f_fi[1]} or self.ids[f'p1{j}'].pos_hint == {"center_x": self.ne_f_fi[0], "center_y": self.ne_f_fi[1]}) and self.ids[f'p1{j}'].icon == "account":
                                    if self.ids[f'p1{j}'].pos_hint == {'center_x': midp11[0], 'center_y': midp11[1]}:
                                        self.ids[f'p1{i}'].text_color = 0,0.2,0.21,0.31   
                    for i in range(1, 21):
                        if (self.ids[f'p2{i}'].pos_hint == {"center_x": self.xe_f_fi[0], "center_y": self.xe_f_fi[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.xne_f_fi[0], "center_y": self.xne_f_fi[1]}) and self.ids[f'p2{i}'].text_color == [0,0.2,0.21,0.31] and self.ids[f'p2{i}'].icon == "record-circle":
                            midp1 = ((self.ids[f'p2{i}'].pos_hint['center_x'] + pb_co[0])/2, (self.ids[f'p2{i}'].pos_hint['center_y'] + pb_co[1])/2)
                            for j in range(1, 21):
                                if (self.ids[f'p2{j}'].pos_hint == {"center_x": self.e_f_fi[0], "center_y": self.e_f_fi[1]} or self.ids[f'p2{j}'].pos_hint == {"center_x": self.ne_f_fi[0], "center_y": self.ne_f_fi[1]}) and self.ids[f'p1{j}'].icon == "account":
                                    if self.ids[f'p2{j}'].pos_hint == {'center_x': midp1[0], 'center_y': midp1[1]}:
                                        self.ids[f'p2{i}'].text_color = 245/255, 5/255, 237/255
                        if (self.ids[f'p1{i}'].pos_hint == {"center_x": self.xe_f_fi[0], "center_y": self.xe_f_fi[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.xne_f_fi[0], "center_y": self.xne_f_fi[1]}) and self.ids[f'p1{i}'].text_color == [0,0.2,0.21,0.31] and self.ids[f'p1{i}'].icon == "record-circle":
                            midp11 = ((self.ids[f'p1{i}'].pos_hint['center_x'] + pb_co[0])/2, (self.ids[f'p1{i}'].pos_hint['center_y'] + pb_co[1])/2)
                            for j in range(1, 21):
                                if (self.ids[f'p2{j}'].pos_hint == {"center_x": self.e_f_fi[0], "center_y": self.e_f_fi[1]} or self.ids[f'p2{j}'].pos_hint == {"center_x": self.ne_f_fi[0], "center_y": self.ne_f_fi[1]}) and self.ids[f'p1{j}'].icon == "account":
                                    if self.ids[f'p2{j}'].pos_hint == {'center_x': midp11[0], 'center_y': midp11[1]}:
                                        self.ids[f'p1{i}'].text_color = 245/255, 5/255, 237/255  
        elif pb_co == (3*x,y):
            self.w_f_fi = (pb_co[0] - x, pb_co[1])
            self.s_f_fi = (pb_co[0], pb_co[1]-y)
            self.nw_f_fi = (pb_co[0] - x, pb_co[1] + y)
            self.sw_f_fi = (pb_co[0] - x, pb_co[1] - y)
            self.se_f_fi = (pb_co[0] + x, pb_co[1] - y)
            self.xw_f_fi = (pb_co[0] - 2*x, pb_co[1])
            self.xnw_f_fi = (pb_co[0] - 2*x, pb_co[1] + 2*y)
            if self.ids.common10.pos_hint == {"center_x": self.w_f_fi[0], "center_y": self.w_f_fi[1]} or self.ids.common10.pos_hint == {"center_x": self.s_f_fi[0], "center_y": self.s_f_fi[1]}or  self.ids.common10.pos_hint == {"center_x": self.sw_f_fi[0], "center_y": self.sw_f_fi[1]} or self.ids.common10.pos_hint == {"center_x": self.se_f_fi[0], "center_y": self.se_f_fi[1]}  or self.ids.common10.pos_hint == {"center_x": self.nw_f_fi[0], "center_y": self.nw_f_fi[1]}:
                self.ids.common10.text_color = 245/255, 5/255, 237/255
            for i in range(1, 21):
                if (self.ids[f'p2{i}'].pos_hint == {"center_x": self.w_f_fi[0], "center_y": self.w_f_fi[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.s_f_fi[0], "center_y": self.s_f_fi[1]}  or self.ids[f'p2{i}'].pos_hint == {"center_x": self.sw_f_fi[0], "center_y": self.sw_f_fi[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.se_f_fi[0], "center_y": self.se_f_fi[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.nw_f_fi[0], "center_y": self.nw_f_fi[1]}) and self.ids[f'p2{i}'].icon == "record-circle" and self.ids[f'p2{i}'].text_color == [0,0.2,0.21,0.31]:
                    self.ids[f'p2{i}'].text_color = 245/255, 5/255, 237/255
                if (self.ids[f'p1{i}'].pos_hint == {"center_x": self.w_f_fi[0], "center_y": self.w_f_fi[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.s_f_fi[0], "center_y": self.s_f_fi[1]}  or self.ids[f'p1{i}'].pos_hint == {"center_x": self.sw_f_fi[0], "center_y": self.sw_f_fi[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.se_f_fi[0], "center_y": self.se_f_fi[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.nw_f_fi[0], "center_y": self.nw_f_fi[1]}) and self.ids[f'p1{i}'].icon == "record-circle" and self.ids[f'p1{i}'].text_color == [0,0.2,0.21,0.31]:
                    self.ids[f'p1{i}'].text_color = 245/255, 5/255, 237/255
            for i in range(1, 21):
                if (self.ids[f'p2{i}'].pos_hint == {"center_x": self.w_f_fi[0], "center_y": self.w_f_fi[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.nw_f_fi[0], "center_y": self.nw_f_fi[1]}) and self.ids[f'p2{i}'].icon != "record-circle":
                    if self.ids.common10.pos_hint == {"center_x": self.xw_f_fi[0], "center_y": self.xw_f_fi[1]} or self.ids.common10.pos_hint == {"center_x": self.xnw_f_fi[0], "center_y": self.xnw_f_fi[1]}:
                        mid = ((self.ids.common10.pos_hint['center_x'] + pb_co[0])/2 , (self.ids.common10.pos_hint['center_y'] + pb_co[1])/2)
                        for j in range(1, 21):
                            if (self.ids[f'p1{j}'].pos_hint == {"center_x": self.w_f_fi[0], "center_y": self.w_f_fi[1]} or self.ids[f'p1{j}'].pos_hint == {"center_x": self.nw_f_fi[0], "center_y": self.nw_f_fi[1]}) and self.ids[f'p1{j}'].icon == "account":
                                if self.ids[f'p1{i}'].pos_hint == {'center_x': mid[0], 'center_y': mid[1]}:
                                    self.ids.common10.text_color = 0,0.2,0.21,0.31  
                        for j in range(1, 21):
                            if (self.ids[f'p2{j}'].pos_hint == {"center_x": self.w_f_fi[0], "center_y": self.w_f_fi[1]} or self.ids[f'p2{j}'].pos_hint == {"center_x": self.nw_f_fi[0], "center_y": self.nw_f_fi[1]}) and self.ids[f'p1{j}'].icon == "account":
                                if self.ids[f'p2{i}'].pos_hint == {'center_x': mid[0], 'center_y': mid[1]}:
                                    self.ids.common10.text_color = 245/255, 5/255, 237/255 
                    for i in range(1, 21):
                        if (self.ids[f'p2{i}'].pos_hint == {"center_x": self.xw_f_fi[0], "center_y": self.xw_f_fi[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.xnw_f_fi[0], "center_y": self.xnw_f_fi[1]}) and self.ids[f'p2{i}'].text_color == [0,0.2,0.21,0.31] and self.ids[f'p2{i}'].icon == "record-circle":
                            midp1 = ((self.ids[f'p2{i}'].pos_hint['center_x'] + pb_co[0])/2, (self.ids[f'p2{i}'].pos_hint['center_y'] + pb_co[1])/2)
                            for j in range(1, 21):
                                if (self.ids[f'p1{j}'].pos_hint == {"center_x": self.w_f_fi[0], "center_y": self.w_f_fi[1]} or self.ids[f'p1{j}'].pos_hint == {"center_x": self.nw_f_fi[0], "center_y": self.nw_f_fi[1]}) and self.ids[f'p1{j}'].icon == "account":
                                    if self.ids[f'p1{j}'].pos_hint == {'center_x': midp1[0], 'center_y': midp1[1]}:
                                        self.ids[f'p2{i}'].text_color = 0,0.2,0.21,0.31   
                        if (self.ids[f'p1{i}'].pos_hint == {"center_x": self.xw_f_fi[0], "center_y": self.xw_f_fi[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.xnw_f_fi[0], "center_y": self.xnw_f_fi[1]}) and self.ids[f'p1{i}'].text_color == [0,0.2,0.21,0.31] and self.ids[f'p1{i}'].icon == "record-circle":
                            midp11 = ((self.ids[f'p1{i}'].pos_hint['center_x'] + pb_co[0])/2, (self.ids[f'p1{i}'].pos_hint['center_y'] + pb_co[1])/2)
                            for j in range(1, 21):
                                if (self.ids[f'p1{j}'].pos_hint == {"center_x": self.w_f_fi[0], "center_y": self.w_f_fi[1]} or self.ids[f'p1{j}'].pos_hint == {"center_x": self.nw_f_fi[0], "center_y": self.nw_f_fi[1]}) and self.ids[f'p1{j}'].icon == "account":
                                    if self.ids[f'p1{j}'].pos_hint == {'center_x': midp11[0], 'center_y': midp11[1]}:
                                        self.ids[f'p1{i}'].text_color = 0,0.2,0.21,0.31   
                    for i in range(1, 21):
                        if (self.ids[f'p2{i}'].pos_hint == {"center_x": self.xw_f_fi[0], "center_y": self.xw_f_fi[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.xnw_f_fi[0], "center_y": self.xnw_f_fi[1]}) and self.ids[f'p2{i}'].text_color == [0,0.2,0.21,0.31] and self.ids[f'p2{i}'].icon == "record-circle":
                            midp1 = ((self.ids[f'p2{i}'].pos_hint['center_x'] + pb_co[0])/2, (self.ids[f'p2{i}'].pos_hint['center_y'] + pb_co[1])/2)
                            for j in range(1, 21):
                                if (self.ids[f'p2{j}'].pos_hint == {"center_x": self.w_f_fi[0], "center_y": self.w_f_fi[1]} or self.ids[f'p2{j}'].pos_hint == {"center_x": self.nw_f_fi[0], "center_y": self.nw_f_fi[1]}) and self.ids[f'p1{j}'].icon == "account":
                                    if self.ids[f'p2{j}'].pos_hint == {'center_x': midp1[0], 'center_y': midp1[1]}:
                                        self.ids[f'p2{i}'].text_color = 245/255, 5/255, 237/255
                        if (self.ids[f'p1{i}'].pos_hint == {"center_x": self.xw_f_fi[0], "center_y": self.xw_f_fi[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.xnw_f_fi[0], "center_y": self.xnw_f_fi[1]}) and self.ids[f'p1{i}'].text_color == [0,0.2,0.21,0.31] and self.ids[f'p1{i}'].icon == "record-circle":
                            midp11 = ((self.ids[f'p1{i}'].pos_hint['center_x'] + pb_co[0])/2, (self.ids[f'p1{i}'].pos_hint['center_y'] + pb_co[1])/2)
                            for j in range(1, 21):
                                if (self.ids[f'p2{j}'].pos_hint == {"center_x": self.w_f_fi[0], "center_y": self.w_f_fi[1]} or self.ids[f'p2{j}'].pos_hint == {"center_x": self.nw_f_fi[0], "center_y": self.nw_f_fi[1]}) and self.ids[f'p1{j}'].icon == "account":
                                    if self.ids[f'p2{j}'].pos_hint == {'center_x': midp11[0], 'center_y': midp11[1]}:
                                        self.ids[f'p1{i}'].text_color = 245/255, 5/255, 237/255  
        elif pb_co == (x,7*y):
            self.e_f_fi = (pb_co[0]+x, pb_co[1])
            self.n_f_fi = (pb_co[0], pb_co[1]+y)
            self.ne_f_fi = (pb_co[0] + x, pb_co[1] + y)
            self.nw_f_fi = (pb_co[0] - x, pb_co[1] + y)
            self.se_f_fi = (pb_co[0] + x, pb_co[1] - y)
            self.xe_f_fi = (pb_co[0]+ 2*x, pb_co[1])
            self.xse_f_fi = (pb_co[0] + 2*x, pb_co[1] - 2*y)
            if self.ids.common10.pos_hint == {"center_x": self.e_f_fi[0], "center_y": self.e_f_fi[1]} or self.ids.common10.pos_hint == {"center_x": self.n_f_fi[0], "center_y": self.n_f_fi[1]}or  self.ids.common10.pos_hint == {"center_x": self.nw_f_fi[0], "center_y": self.nw_f_fi[1]} or self.ids.common10.pos_hint == {"center_x": self.se_f_fi[0], "center_y": self.se_f_fi[1]}  or self.ids.common10.pos_hint == {"center_x": self.ne_f_fi[0], "center_y": self.ne_f_fi[1]}:
                self.ids.common10.text_color = 245/255, 5/255, 237/255
            for i in range(1, 21):
                if (self.ids[f'p2{i}'].pos_hint == {"center_x": self.e_f_fi[0], "center_y": self.e_f_fi[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.n_f_fi[0], "center_y": self.n_f_fi[1]}  or self.ids[f'p2{i}'].pos_hint == {"center_x": self.nw_f_fi[0], "center_y": self.nw_f_fi[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.se_f_fi[0], "center_y": self.se_f_fi[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.ne_f_fi[0], "center_y": self.ne_f_fi[1]}) and self.ids[f'p2{i}'].icon == "record-circle" and self.ids[f'p2{i}'].text_color == [0,0.2,0.21,0.31]:
                    self.ids[f'p2{i}'].text_color = 245/255, 5/255, 237/255
                if (self.ids[f'p1{i}'].pos_hint == {"center_x": self.e_f_fi[0], "center_y": self.e_f_fi[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.n_f_fi[0], "center_y": self.n_f_fi[1]}  or self.ids[f'p1{i}'].pos_hint == {"center_x": self.nw_f_fi[0], "center_y": self.nw_f_fi[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.se_f_fi[0], "center_y": self.se_f_fi[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.ne_f_fi[0], "center_y": self.ne_f_fi[1]}) and self.ids[f'p1{i}'].icon == "record-circle" and self.ids[f'p1{i}'].text_color == [0,0.2,0.21,0.31]:
                    self.ids[f'p1{i}'].text_color = 245/255, 5/255, 237/255
            for i in range(1, 21):
                if (self.ids[f'p2{i}'].pos_hint == {"center_x": self.e_f_fi[0], "center_y": self.e_f_fi[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.se_f_fi[0], "center_y": self.se_f_fi[1]}) and self.ids[f'p2{i}'].icon != "record-circle":
                    if self.ids.common10.pos_hint == {"center_x": self.xe_f_fi[0], "center_y": self.xe_f_fi[1]} or self.ids.common10.pos_hint == {"center_x": self.xse_f_fi[0], "center_y": self.xse_f_fi[1]}:
                        mid = ((self.ids.common10.pos_hint['center_x'] + pb_co[0])/2 , (self.ids.common10.pos_hint['center_y'] + pb_co[1])/2)
                        for j in range(1, 21):
                            if (self.ids[f'p1{j}'].pos_hint == {"center_x": self.e_f_fi[0], "center_y": self.e_f_fi[1]} or self.ids[f'p1{j}'].pos_hint == {"center_x": self.se_f_fi[0], "center_y": self.se_f_fi[1]}) and self.ids[f'p1{j}'].icon == "account":
                                if self.ids[f'p1{i}'].pos_hint == {'center_x': mid[0], 'center_y': mid[1]}:
                                    self.ids.common10.text_color = 0,0.2,0.21,0.31  
                        for j in range(1, 21):
                            if (self.ids[f'p2{j}'].pos_hint == {"center_x": self.e_f_fi[0], "center_y": self.e_f_fi[1]} or self.ids[f'p2{j}'].pos_hint == {"center_x": self.se_f_fi[0], "center_y": self.se_f_fi[1]}) and self.ids[f'p1{j}'].icon == "account":
                                if self.ids[f'p2{i}'].pos_hint == {'center_x': mid[0], 'center_y': mid[1]}:
                                    self.ids.common10.text_color = 245/255, 5/255, 237/255 
                    for i in range(1, 21):
                        if (self.ids[f'p2{i}'].pos_hint == {"center_x": self.xe_f_fi[0], "center_y": self.xe_f_fi[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.xse_f_fi[0], "center_y": self.xse_f_fi[1]}) and self.ids[f'p2{i}'].text_color == [0,0.2,0.21,0.31] and self.ids[f'p2{i}'].icon == "record-circle":
                            midp1 = ((self.ids[f'p2{i}'].pos_hint['center_x'] + pb_co[0])/2, (self.ids[f'p2{i}'].pos_hint['center_y'] + pb_co[1])/2)
                            for j in range(1, 21):
                                if (self.ids[f'p1{j}'].pos_hint == {"center_x": self.e_f_fi[0], "center_y": self.e_f_fi[1]} or self.ids[f'p1{j}'].pos_hint == {"center_x": self.se_f_fi[0], "center_y": self.se_f_fi[1]}) and self.ids[f'p1{j}'].icon == "account":
                                    if self.ids[f'p1{j}'].pos_hint == {'center_x': midp1[0], 'center_y': midp1[1]}:
                                        self.ids[f'p2{i}'].text_color = 0,0.2,0.21,0.31   
                        if (self.ids[f'p1{i}'].pos_hint == {"center_x": self.xe_f_fi[0], "center_y": self.xe_f_fi[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.xse_f_fi[0], "center_y": self.xse_f_fi[1]}) and self.ids[f'p1{i}'].text_color == [0,0.2,0.21,0.31] and self.ids[f'p1{i}'].icon == "record-circle":
                            midp11 = ((self.ids[f'p1{i}'].pos_hint['center_x'] + pb_co[0])/2, (self.ids[f'p1{i}'].pos_hint['center_y'] + pb_co[1])/2)
                            for j in range(1, 21):
                                if (self.ids[f'p1{j}'].pos_hint == {"center_x": self.e_f_fi[0], "center_y": self.e_f_fi[1]} or self.ids[f'p1{j}'].pos_hint == {"center_x": self.se_f_fi[0], "center_y": self.se_f_fi[1]}) and self.ids[f'p1{j}'].icon == "account":
                                    if self.ids[f'p1{j}'].pos_hint == {'center_x': midp11[0], 'center_y': midp11[1]}:
                                        self.ids[f'p1{i}'].text_color = 0,0.2,0.21,0.31   
                    for i in range(1, 21):
                        if (self.ids[f'p2{i}'].pos_hint == {"center_x": self.xe_f_fi[0], "center_y": self.xe_f_fi[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.xse_f_fi[0], "center_y": self.xse_f_fi[1]}) and self.ids[f'p2{i}'].text_color == [0,0.2,0.21,0.31] and self.ids[f'p2{i}'].icon == "record-circle":
                            midp1 = ((self.ids[f'p2{i}'].pos_hint['center_x'] + pb_co[0])/2, (self.ids[f'p2{i}'].pos_hint['center_y'] + pb_co[1])/2)
                            for j in range(1, 21):
                                if (self.ids[f'p2{j}'].pos_hint == {"center_x": self.e_f_fi[0], "center_y": self.e_f_fi[1]} or self.ids[f'p2{j}'].pos_hint == {"center_x": self.se_f_fi[0], "center_y": self.se_f_fi[1]}) and self.ids[f'p2{j}'].icon == "account":
                                    if self.ids[f'p2{j}'].pos_hint == {'center_x': midp1[0], 'center_y': midp1[1]}:
                                        self.ids[f'p2{i}'].text_color = 245/255, 5/255, 237/255
                        if (self.ids[f'p1{i}'].pos_hint == {"center_x": self.xe_f_fi[0], "center_y": self.xe_f_fi[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.xse_f_fi[0], "center_y": self.xse_f_fi[1]}) and self.ids[f'p1{i}'].text_color == [0,0.2,0.21,0.31] and self.ids[f'p1{i}'].icon == "record-circle":
                            midp11 = ((self.ids[f'p1{i}'].pos_hint['center_x'] + pb_co[0])/2, (self.ids[f'p1{i}'].pos_hint['center_y'] + pb_co[1])/2)
                            for j in range(1, 21):
                                if (self.ids[f'p2{j}'].pos_hint == {"center_x": self.e_f_fi[0], "center_y": self.e_f_fi[1]} or self.ids[f'p2{j}'].pos_hint == {"center_x": self.se_f_fi[0], "center_y": self.se_f_fi[1]}) and self.ids[f'p2{j}'].icon == "account":
                                    if self.ids[f'p2{j}'].pos_hint == {'center_x': midp11[0], 'center_y': midp11[1]}:
                                        self.ids[f'p1{i}'].text_color = 245/255, 5/255, 237/255  
        elif pb_co == (3*x,7*y):
            self.w_f_fi = (pb_co[0] - x, pb_co[1])
            self.n_f_fi = (pb_co[0], pb_co[1]+y)
            self.ne_f_fi = (pb_co[0] + x, pb_co[1] + y)
            self.nw_f_fi = (pb_co[0] - x, pb_co[1] + y)
            self.sw_f_fi = (pb_co[0] - x, pb_co[1] - y)
            self.xw_f_fi = (pb_co[0] - 2*x, pb_co[1])
            self.xsw_f_fi = (pb_co[0] - 2*x, pb_co[1] - 2*y)
            if self.ids.common10.pos_hint == {"center_x": self.w_f_fi[0], "center_y": self.w_f_fi[1]} or self.ids.common10.pos_hint == {"center_x": self.n_f_fi[0], "center_y": self.n_f_fi[1]}or  self.ids.common10.pos_hint == {"center_x": self.sw_f_fi[0], "center_y": self.sw_f_fi[1]} or self.ids.common10.pos_hint == {"center_x": self.ne_f_fi[0], "center_y": self.ne_f_fi[1]}  or self.ids.common10.pos_hint == {"center_x": self.nw_f_fi[0], "center_y": self.nw_f_fi[1]}:
                self.ids.common10.text_color = 245/255, 5/255, 237/255
            for i in range(1, 21):
                if (self.ids[f'p2{i}'].pos_hint == {"center_x": self.w_f_fi[0], "center_y": self.w_f_fi[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.n_f_fi[0], "center_y": self.n_f_fi[1]}  or self.ids[f'p2{i}'].pos_hint == {"center_x": self.sw_f_fi[0], "center_y": self.sw_f_fi[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.ne_f_fi[0], "center_y": self.ne_f_fi[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.nw_f_fi[0], "center_y": self.nw_f_fi[1]}) and self.ids[f'p2{i}'].icon == "record-circle" and self.ids[f'p2{i}'].text_color == [0,0.2,0.21,0.31]:
                    self.ids[f'p2{i}'].text_color = 245/255, 5/255, 237/255
                if (self.ids[f'p1{i}'].pos_hint == {"center_x": self.w_f_fi[0], "center_y": self.w_f_fi[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.n_f_fi[0], "center_y": self.n_f_fi[1]}  or self.ids[f'p1{i}'].pos_hint == {"center_x": self.sw_f_fi[0], "center_y": self.sw_f_fi[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.ne_f_fi[0], "center_y": self.ne_f_fi[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.nw_f_fi[0], "center_y": self.nw_f_fi[1]}) and self.ids[f'p1{i}'].icon == "record-circle" and self.ids[f'p1{i}'].text_color == [0,0.2,0.21,0.31]:
                    self.ids[f'p1{i}'].text_color = 245/255, 5/255, 237/255
            for i in range(1, 21):
                if (self.ids[f'p2{i}'].pos_hint == {"center_x": self.w_f_fi[0], "center_y": self.w_f_fi[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.sw_f_fi[0], "center_y": self.sw_f_fi[1]}) and self.ids[f'p2{i}'].icon != "record-circle":
                    if self.ids.common10.pos_hint == {"center_x": self.xw_f_fi[0], "center_y": self.xw_f_fi[1]} or self.ids.common10.pos_hint == {"center_x": self.xsw_f_fi[0], "center_y": self.xsw_f_fi[1]}:
                        mid = ((self.ids.common10.pos_hint['center_x'] + pb_co[0])/2 , (self.ids.common10.pos_hint['center_y'] + pb_co[1])/2)
                        for j in range(1, 21):
                            if (self.ids[f'p1{j}'].pos_hint == {"center_x": self.w_f_fi[0], "center_y": self.w_f_fi[1]} or self.ids[f'p1{j}'].pos_hint == {"center_x": self.sw_f_fi[0], "center_y": self.sw_f_fi[1]}) and self.ids[f'p1{j}'].icon == "account":
                                if self.ids[f'p1{j}'].pos_hint == {'center_x': mid[0], 'center_y': mid[1]}:
                                    self.ids.common10.text_color = 0,0.2,0.21,0.31  
                        for j in range(1, 21):
                            if (self.ids[f'p2{j}'].pos_hint == {"center_x": self.w_f_fi[0], "center_y": self.w_f_fi[1]} or self.ids[f'p2{j}'].pos_hint == {"center_x": self.sw_f_fi[0], "center_y": self.sw_f_fi[1]}) and self.ids[f'p2{j}'].icon == "account":
                                if self.ids[f'p2{j}'].pos_hint == {'center_x': mid[0], 'center_y': mid[1]}:
                                    self.ids.common10.text_color = 245/255, 5/255, 237/255 
                    for i in range(1, 21):
                        if (self.ids[f'p2{i}'].pos_hint == {"center_x": self.xw_f_fi[0], "center_y": self.xw_f_fi[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.xsw_f_fi[0], "center_y": self.xsw_f_fi[1]}) and self.ids[f'p2{i}'].text_color == [0,0.2,0.21,0.31] and self.ids[f'p2{i}'].icon == "record-circle":
                            midp1 = ((self.ids[f'p2{i}'].pos_hint['center_x'] + pb_co[0])/2, (self.ids[f'p2{i}'].pos_hint['center_y'] + pb_co[1])/2)
                            for j in range(1, 21):
                                if (self.ids[f'p1{j}'].pos_hint == {"center_x": self.w_f_fi[0], "center_y": self.w_f_fi[1]} or self.ids[f'p1{j}'].pos_hint == {"center_x": self.sw_f_fi[0], "center_y": self.sw_f_fi[1]}) and self.ids[f'p1{j}'].icon == "account":
                                    if self.ids[f'p1{j}'].pos_hint == {'center_x': midp1[0], 'center_y': midp1[1]}:
                                        self.ids[f'p2{i}'].text_color = 0,0.2,0.21,0.31   
                        if (self.ids[f'p1{i}'].pos_hint == {"center_x": self.xw_f_fi[0], "center_y": self.xw_f_fi[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.xsw_f_fi[0], "center_y": self.xsw_f_fi[1]}) and self.ids[f'p1{i}'].text_color == [0,0.2,0.21,0.31] and self.ids[f'p1{i}'].icon == "record-circle":
                            midp11 = ((self.ids[f'p1{i}'].pos_hint['center_x'] + pb_co[0])/2, (self.ids[f'p1{i}'].pos_hint['center_y'] + pb_co[1])/2)
                            for j in range(1, 21):
                                if (self.ids[f'p1{j}'].pos_hint == {"center_x": self.w_f_fi[0], "center_y": self.w_f_fi[1]} or self.ids[f'p1{j}'].pos_hint == {"center_x": self.sw_f_fi[0], "center_y": self.sw_f_fi[1]}) and self.ids[f'p1{j}'].icon == "account":
                                    if self.ids[f'p1{j}'].pos_hint == {'center_x': midp11[0], 'center_y': midp11[1]}:
                                        self.ids[f'p1{i}'].text_color = 0,0.2,0.21,0.31   
                    for i in range(1, 21):
                        if (self.ids[f'p2{i}'].pos_hint == {"center_x": self.xw_f_fi[0], "center_y": self.xw_f_fi[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.xsw_f_fi[0], "center_y": self.xsw_f_fi[1]}) and self.ids[f'p2{i}'].text_color == [0,0.2,0.21,0.31] and self.ids[f'p2{i}'].icon == "record-circle":
                            midp1 = ((self.ids[f'p2{i}'].pos_hint['center_x'] + pb_co[0])/2, (self.ids[f'p2{i}'].pos_hint['center_y'] + pb_co[1])/2)
                            for j in range(1, 21):
                                if (self.ids[f'p2{j}'].pos_hint == {"center_x": self.w_f_fi[0], "center_y": self.w_f_fi[1]} or self.ids[f'p2{j}'].pos_hint == {"center_x": self.sw_f_fi[0], "center_y": self.sw_f_fi[1]}) and self.ids[f'p2{j}'].icon == "account":
                                    if self.ids[f'p2{j}'].pos_hint == {'center_x': midp1[0], 'center_y': midp1[1]}:
                                        self.ids[f'p2{i}'].text_color = 245/255, 5/255, 237/255
                        if (self.ids[f'p1{i}'].pos_hint == {"center_x": self.xw_f_fi[0], "center_y": self.xw_f_fi[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.xsw_f_fi[0], "center_y": self.xsw_f_fi[1]}) and self.ids[f'p1{i}'].text_color == [0,0.2,0.21,0.31] and self.ids[f'p1{i}'].icon == "record-circle":
                            midp11 = ((self.ids[f'p1{i}'].pos_hint['center_x'] + pb_co[0])/2, (self.ids[f'p1{i}'].pos_hint['center_y'] + pb_co[1])/2)
                            for j in range(1, 21):
                                if (self.ids[f'p2{j}'].pos_hint == {"center_x": self.w_f_fi[0], "center_y": self.w_f_fi[1]} or self.ids[f'p2{j}'].pos_hint == {"center_x": self.sw_f_fi[0], "center_y": self.sw_f_fi[1]}) and self.ids[f'p2{j}'].icon == "account":
                                    if self.ids[f'p2{j}'].pos_hint == {'center_x': midp11[0], 'center_y': midp11[1]}:
                                        self.ids[f'p1{i}'].text_color = 245/255, 5/255, 237/255  

    def player2(self, second):
        x = 0.25
        y = 0.125
        self.button_clicked.play()
        for i in range(1, 21):
            if self.ids[f'p1{i}'].icon == "account": 
                self.ids[f'p1{i}'].disabled = True
                self.ids[f'p1{i}'].disabled_color = self.player1_color
        self.ids[f'common10'].text_color =  0,0.2,0.21,0.31
        for i in range(1, 21):
            if self.ids[f'p1{i}'].icon == "record-circle" or self.ids[f'p1{i}'].text_color == [245/255, 5/255, 237/255]:
                self.ids[f'p1{i}'].text_color = 0,0.2,0.21,0.31
        for i in range(1, 21):
            if self.ids[f'p2{i}'].icon == "record-circle" or self.ids[f'p2{i}'].text_color == [245/255, 5/255, 237/255]:
                self.ids[f'p2{i}'].text_color = 0,0.2,0.21,0.31
        self.p1 = second
        points = second.pos_hint
        pb_co = (points['center_x'], points['center_y'])
        if pb_co == (0, 2*y) or pb_co == (2*x, 2*y) or pb_co == (2*x, 0) or pb_co == (4*x, 2*y) or pb_co == (x, 3*y) or pb_co == (3*x, 3*y) or pb_co == (0, 4*y) or pb_co == (4*x, 4*y) or pb_co == (x, 5*y) or pb_co == (3*x, 5*y) or pb_co == (0, 6*y) or pb_co == (2*x, 6*y) or pb_co == (4*x, 6*y) or pb_co == (2*x, 4*y) or pb_co == (0,0) or pb_co == (4*x, 0) or pb_co==(0, 8*y) or pb_co==(2*x, 8*y) or pb_co==(4*x, 8*y):
            self.w_f_se = (pb_co[0] - x, pb_co[1])
            self.e_f_se = (pb_co[0]+x, pb_co[1])
            self.n_f_se = (pb_co[0], pb_co[1]+y)
            self.s_f_se = (pb_co[0], pb_co[1]-y)
            self.ne_f_se = (pb_co[0] + x, pb_co[1] + y)
            self.nw_f_se = (pb_co[0] - x, pb_co[1] + y)
            self.sw_f_se = (pb_co[0] - x, pb_co[1] - y)
            self.se_f_se = (pb_co[0] + x, pb_co[1] - y)
            self.xw_f_se = (pb_co[0] - 2*x, pb_co[1])
            self.xe_f_se = (pb_co[0]+ 2*x, pb_co[1])
            self.xn_f_se = (pb_co[0], pb_co[1]+2*y)
            self.xs_f_se = (pb_co[0], pb_co[1]-2*y)
            self.xne_f_se = (pb_co[0] + 2*x, pb_co[1] + 2*y)
            self.xnw_f_se = (pb_co[0] - 2*x, pb_co[1] + 2*y)
            self.xsw_f_se = (pb_co[0] - 2*x, pb_co[1] - 2*y)
            self.xse_f_se = (pb_co[0] + 2*x, pb_co[1] - 2*y)
            if self.ids.common10.pos_hint == {"center_x": self.w_f_se[0], "center_y": self.w_f_se[1]} or self.ids.common10.pos_hint == {"center_x": self.e_f_se[0], "center_y": self.e_f_se[1]} or self.ids.common10.pos_hint == {"center_x": self.s_f_se[0], "center_y": self.s_f_se[1]} or self.ids.common10.pos_hint == {"center_x": self.n_f_se[0], "center_y": self.n_f_se[1]} or self.ids.common10.pos_hint == {"center_x": self.sw_f_se[0], "center_y": self.sw_f_se[1]} or self.ids.common10.pos_hint == {"center_x": self.se_f_se[0], "center_y": self.se_f_se[1]} or self.ids.common10.pos_hint == {"center_x": self.nw_f_se[0], "center_y": self.nw_f_se[1]} or self.ids.common10.pos_hint == {"center_x": self.ne_f_se[0], "center_y": self.ne_f_se[1]}:
                self.ids.common10.text_color = 245/255, 5/255, 237/255
            for i in range(1, 21):
                if (self.ids[f'p1{i}'].pos_hint == {"center_x": self.w_f_se[0], "center_y": self.w_f_se[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.e_f_se[0], "center_y": self.e_f_se[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.s_f_se[0], "center_y": self.s_f_se[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.n_f_se[0], "center_y": self.n_f_se[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.sw_f_se[0], "center_y": self.sw_f_se[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.se_f_se[0], "center_y": self.se_f_se[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.nw_f_se[0], "center_y": self.nw_f_se[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.ne_f_se[0], "center_y": self.ne_f_se[1]}) and self.ids[f'p1{i}'].icon == "record-circle" and self.ids[f'p1{i}'].text_color == [0,0.2,0.21,0.31]:
                    self.ids[f'p1{i}'].text_color = 245/255, 5/255, 237/255
                if (self.ids[f'p2{i}'].pos_hint == {"center_x": self.w_f_se[0], "center_y": self.w_f_se[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.e_f_se[0], "center_y": self.e_f_se[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.s_f_se[0], "center_y": self.s_f_se[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.n_f_se[0], "center_y": self.n_f_se[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.sw_f_se[0], "center_y": self.sw_f_se[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.se_f_se[0], "center_y": self.se_f_se[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.nw_f_se[0], "center_y": self.nw_f_se[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.ne_f_se[0], "center_y": self.ne_f_se[1]})  and self.ids[f'p2{i}'].icon == "record-circle" and self.ids[f'p2{i}'].text_color == [0,0.2,0.21,0.31]:
                    self.ids[f'p2{i}'].text_color = 245/255, 5/255, 237/255
            for i in range(1, 21):
                if (self.ids[f'p1{i}'].pos_hint == {"center_x": self.n_f_se[0], "center_y": self.n_f_se[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.s_f_se[0], "center_y": self.s_f_se[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.e_f_se[0], "center_y": self.e_f_se[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.w_f_se[0], "center_y": self.w_f_se[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.nw_f_se[0], "center_y": self.nw_f_se[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.ne_f_se[0], "center_y": self.ne_f_se[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.sw_f_se[0], "center_y": self.sw_f_se[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.se_f_se[0], "center_y": self.se_f_se[1]}) and self.ids[f'p1{i}'].icon != "record-circle":
                    if self.ids.common10.pos_hint == {"center_x": self.xw_f_se[0], "center_y": self.xw_f_se[1]} or self.ids.common10.pos_hint == {"center_x": self.xe_f_se[0], "center_y": self.xe_f_se[1]} or self.ids.common10.pos_hint == {"center_x": self.xs_f_se[0], "center_y": self.xs_f_se[1]} or self.ids.common10.pos_hint == {"center_x": self.xn_f_se[0], "center_y": self.xn_f_se[1]} or self.ids.common10.pos_hint == {"center_x": self.xnw_f_se[0], "center_y": self.xnw_f_se[1]} or self.ids.common10.pos_hint == {"center_x": self.xsw_f_se[0], "center_y": self.xsw_f_se[1]} or self.ids.common10.pos_hint == {"center_x": self.xse_f_se[0], "center_y": self.xse_f_se[1]} or self.ids.common10.pos_hint == {"center_x": self.xne_f_se[0], "center_y": self.xne_f_se[1]}:
                        mid = ((self.ids.common10.pos_hint['center_x'] + pb_co[0])/2 , (self.ids.common10.pos_hint['center_y'] + pb_co[1])/2)
                        for j in range(1, 21):
                            if (self.ids[f'p2{j}'].pos_hint == {"center_x": self.w_f_se[0], "center_y": self.w_f_se[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.e_f_se[0], "center_y": self.e_f_se[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.s_f_se[0], "center_y": self.s_f_se[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.n_f_se[0], "center_y": self.n_f_se[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.sw_f_se[0], "center_y": self.sw_f_se[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.se_f_se[0], "center_y": self.se_f_se[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.nw_f_se[0], "center_y": self.nw_f_se[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.ne_f_se[0], "center_y": self.ne_f_se[1]}) and self.ids[f'p2{i}'].icon == "account":
                                if self.ids[f'p2{i}'].pos_hint == {'center_x': mid[0], 'center_y': mid[1]}:
                                    self.ids.common10.text_color = 0,0.2,0.21,0.31  
                        for j in range(1, 21):
                            if (self.ids[f'p1{j}'].pos_hint == {"center_x": self.w_f_se[0], "center_y": self.w_f_se[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.e_f_se[0], "center_y": self.e_f_se[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.s_f_se[0], "center_y": self.s_f_se[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.n_f_se[0], "center_y": self.n_f_se[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.sw_f_se[0], "center_y": self.sw_f_se[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.se_f_se[0], "center_y": self.se_f_se[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.nw_f_se[0], "center_y": self.nw_f_se[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.ne_f_se[0], "center_y": self.ne_f_se[1]}) and self.ids[f'p1{i}'].icon == "account":
                                if self.ids[f'p1{i}'].pos_hint == {'center_x': mid[0], 'center_y': mid[1]}:
                                    self.ids.common10.text_color = 245/255, 5/255, 237/255
                    for i in range(1, 21):
                        if (self.ids[f'p2{i}'].pos_hint == {"center_x": self.xn_f_se[0], "center_y": self.xn_f_se[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.xw_f_se[0], "center_y": self.xw_f_se[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.xs_f_se[0], "center_y": self.xs_f_se[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.xe_f_se[0], "center_y": self.xe_f_se[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.xne_f_se[0], "center_y": self.xne_f_se[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.xnw_f_se[0], "center_y": self.xnw_f_se[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.xsw_f_se[0], "center_y": self.xsw_f_se[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.xse_f_se[0], "center_y": self.xse_f_se[1]}) and self.ids[f'p2{i}'].text_color == [0,0.2,0.21,0.31] and self.ids[f'p2{i}'].icon == "record-circle":
                            midp21 = ((self.ids[f'p2{i}'].pos_hint['center_x'] + pb_co[0])/2, (self.ids[f'p2{i}'].pos_hint['center_y'] + pb_co[1])/2)
                            for j in range(1, 21):
                                if (self.ids[f'p2{j}'].pos_hint == {"center_x": self.w_f_se[0], "center_y": self.w_f_se[1]} or self.ids[f'p2{j}'].pos_hint == {"center_x": self.e_f_se[0], "center_y": self.e_f_se[1]} or self.ids[f'p2{j}'].pos_hint == {"center_x": self.s_f_se[0], "center_y": self.s_f_se[1]} or self.ids[f'p2{j}'].pos_hint == {"center_x": self.n_f_se[0], "center_y": self.n_f_se[1]} or self.ids[f'p2{j}'].pos_hint == {"center_x": self.sw_f_se[0], "center_y": self.sw_f_se[1]} or self.ids[f'p2{j}'].pos_hint == {"center_x": self.se_f_se[0], "center_y": self.se_f_se[1]} or self.ids[f'p2{j}'].pos_hint == {"center_x": self.nw_f_se[0], "center_y": self.nw_f_se[1]} or self.ids[f'p2{j}'].pos_hint == {"center_x": self.ne_f_se[0], "center_y": self.ne_f_se[1]}) and self.ids[f'p2{j}'].icon == "account":
                                    if self.ids[f'p2{j}'].pos_hint == {'center_x': midp21[0], 'center_y': midp21[1]}:
                                        self.ids[f'p2{i}'].text_color = 0,0.2,0.21,0.31   
                        if (self.ids[f'p1{i}'].pos_hint == {"center_x": self.xn_f_se[0], "center_y": self.xn_f_se[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.xw_f_se[0], "center_y": self.xw_f_se[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.xs_f_se[0], "center_y": self.xs_f_se[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.xe_f_se[0], "center_y": self.xe_f_se[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.xne_f_se[0], "center_y": self.xne_f_se[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.xnw_f_se[0], "center_y": self.xnw_f_se[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.xsw_f_se[0], "center_y": self.xsw_f_se[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.xse_f_se[0], "center_y": self.xse_f_se[1]}) and self.ids[f'p1{i}'].text_color == [0,0.2,0.21,0.31] and self.ids[f'p1{i}'].icon == "record-circle":
                            midp211 = ((self.ids[f'p1{i}'].pos_hint['center_x'] + pb_co[0])/2, (self.ids[f'p1{i}'].pos_hint['center_y'] + pb_co[1])/2)
                            for j in range(1, 21):
                                if (self.ids[f'p2{j}'].pos_hint == {"center_x": self.w_f_se[0], "center_y": self.w_f_se[1]} or self.ids[f'p2{j}'].pos_hint == {"center_x": self.e_f_se[0], "center_y": self.e_f_se[1]} or self.ids[f'p2{j}'].pos_hint == {"center_x": self.s_f_se[0], "center_y": self.s_f_se[1]} or self.ids[f'p2{j}'].pos_hint == {"center_x": self.n_f_se[0], "center_y": self.n_f_se[1]} or self.ids[f'p2{j}'].pos_hint == {"center_x": self.sw_f_se[0], "center_y": self.sw_f_se[1]} or self.ids[f'p2{j}'].pos_hint == {"center_x": self.se_f_se[0], "center_y": self.se_f_se[1]} or self.ids[f'p2{j}'].pos_hint == {"center_x": self.nw_f_se[0], "center_y": self.nw_f_se[1]} or self.ids[f'p2{j}'].pos_hint == {"center_x": self.ne_f_se[0], "center_y": self.ne_f_se[1]}) and self.ids[f'p2{j}'].icon == "account":
                                    if self.ids[f'p2{j}'].pos_hint == {'center_x': midp211[0], 'center_y': midp211[1]}:
                                        self.ids[f'p1{i}'].text_color = 0,0.2,0.21,0.31   
                    for i in range(1, 21):
                        if (self.ids[f'p2{i}'].pos_hint == {"center_x": self.xn_f_se[0], "center_y": self.xn_f_se[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.xw_f_se[0], "center_y": self.xw_f_se[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.xs_f_se[0], "center_y": self.xs_f_se[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.xe_f_se[0], "center_y": self.xe_f_se[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.xne_f_se[0], "center_y": self.xne_f_se[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.xnw_f_se[0], "center_y": self.xnw_f_se[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.xsw_f_se[0], "center_y": self.xsw_f_se[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.xse_f_se[0], "center_y": self.xse_f_se[1]}) and self.ids[f'p2{i}'].text_color == [0,0.2,0.21,0.31] and self.ids[f'p2{i}'].icon == "record-circle":
                            midp31 = ((self.ids[f'p2{i}'].pos_hint['center_x'] + pb_co[0])/2, (self.ids[f'p2{i}'].pos_hint['center_y'] + pb_co[1])/2)
                            for j in range(1, 21):
                                if (self.ids[f'p1{j}'].pos_hint == {"center_x": self.w_f_se[0], "center_y": self.w_f_se[1]} or self.ids[f'p1{j}'].pos_hint == {"center_x": self.e_f_se[0], "center_y": self.e_f_se[1]} or self.ids[f'p1{j}'].pos_hint == {"center_x": self.s_f_se[0], "center_y": self.s_f_se[1]} or self.ids[f'p1{j}'].pos_hint == {"center_x": self.n_f_se[0], "center_y": self.n_f_se[1]} or self.ids[f'p1{j}'].pos_hint == {"center_x": self.sw_f_se[0], "center_y": self.sw_f_se[1]} or self.ids[f'p1{j}'].pos_hint == {"center_x": self.se_f_se[0], "center_y": self.se_f_se[1]} or self.ids[f'p1{j}'].pos_hint == {"center_x": self.nw_f_se[0], "center_y": self.nw_f_se[1]} or self.ids[f'p1{j}'].pos_hint == {"center_x": self.ne_f_se[0], "center_y": self.ne_f_se[1]}) and self.ids[f'p1{j}'].icon == "account":
                                    if self.ids[f'p1{j}'].pos_hint == {'center_x': midp31[0], 'center_y': midp31[1]}:
                                        self.ids[f'p2{i}'].text_color = 245/255, 5/255, 237/255  
                        if (self.ids[f'p1{i}'].pos_hint == {"center_x": self.xn_f_se[0], "center_y": self.xn_f_se[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.xw_f_se[0], "center_y": self.xw_f_se[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.xs_f_se[0], "center_y": self.xs_f_se[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.xe_f_se[0], "center_y": self.xe_f_se[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.xne_f_se[0], "center_y": self.xne_f_se[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.xnw_f_se[0], "center_y": self.xnw_f_se[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.xsw_f_se[0], "center_y": self.xsw_f_se[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.xse_f_se[0], "center_y": self.xse_f_se[1]}) and self.ids[f'p1{i}'].text_color == [0,0.2,0.21,0.31] and self.ids[f'p1{i}'].icon == "record-circle":
                            midp311 = ((self.ids[f'p1{i}'].pos_hint['center_x'] + pb_co[0])/2, (self.ids[f'p1{i}'].pos_hint['center_y'] + pb_co[1])/2)
                            for j in range(1, 21):
                                if (self.ids[f'p1{j}'].pos_hint == {"center_x": self.w_f_se[0], "center_y": self.w_f_se[1]} or self.ids[f'p1{j}'].pos_hint == {"center_x": self.e_f_se[0], "center_y": self.e_f_se[1]} or self.ids[f'p1{j}'].pos_hint == {"center_x": self.s_f_se[0], "center_y": self.s_f_se[1]} or self.ids[f'p1{j}'].pos_hint == {"center_x": self.n_f_se[0], "center_y": self.n_f_se[1]} or self.ids[f'p1{j}'].pos_hint == {"center_x": self.sw_f_se[0], "center_y": self.sw_f_se[1]} or self.ids[f'p1{j}'].pos_hint == {"center_x": self.se_f_se[0], "center_y": self.se_f_se[1]} or self.ids[f'p1{j}'].pos_hint == {"center_x": self.nw_f_se[0], "center_y": self.nw_f_se[1]} or self.ids[f'p1{j}'].pos_hint == {"center_x": self.ne_f_se[0], "center_y": self.ne_f_se[1]}) and self.ids[f'p1{j}'].icon == "account":
                                    if self.ids[f'p1{j}'].pos_hint == {'center_x': midp311[0], 'center_y': midp311[1]}:
                                        self.ids[f'p1{i}'].text_color = 245/255, 5/255, 237/255  
                    
        elif pb_co == (0,3*y) or pb_co == (2*x, 3*y) or pb_co == (4*x, 3*y) or pb_co == (x,4*y) or pb_co == (3*x,4*y) or pb_co == (0,5*y) or pb_co == (2*x,5*y) or pb_co==(4*x,5*y) or pb_co == (2*x, y) or pb_co == (x,0) or pb_co == (3*x, 0) or pb_co == (x,8*y) or pb_co == (3*x, 8*y) or pb_co==(2*x, 7*y):
            self.w_f_se = (pb_co[0] - x, pb_co[1])
            self.e_f_se = (pb_co[0]+x, pb_co[1])
            self.n_f_se = (pb_co[0], pb_co[1]+y)
            self.s_f_se = (pb_co[0], pb_co[1]-y)
            self.xw_f_se = (pb_co[0] - 2*x, pb_co[1])
            self.xe_f_se = (pb_co[0]+2*x, pb_co[1])
            self.xn_f_se = (pb_co[0], pb_co[1]+2*y)
            self.xs_f_se = (pb_co[0], pb_co[1]-2*y)
            if self.ids.common10.pos_hint == {"center_x": self.w_f_se[0], "center_y": self.w_f_se[1]} or self.ids.common10.pos_hint == {"center_x": self.e_f_se[0], "center_y": self.e_f_se[1]} or self.ids.common10.pos_hint == {"center_x": self.s_f_se[0], "center_y": self.s_f_se[1]} or self.ids.common10.pos_hint == {"center_x": self.n_f_se[0], "center_y": self.n_f_se[1]}:
                self.ids.common10.text_color = 245/255, 5/255, 237/255
            for i in range(1, 21):
                if (self.ids[f'p1{i}'].pos_hint == {"center_x": self.w_f_se[0], "center_y": self.w_f_se[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.e_f_se[0], "center_y": self.e_f_se[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.s_f_se[0], "center_y": self.s_f_se[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.n_f_se[0], "center_y": self.n_f_se[1]}) and self.ids[f'p1{i}'].text_color == [0,0.2,0.21,0.31] and self.ids[f'p1{i}'].icon == "record-circle":
                    self.ids[f'p1{i}'].text_color = 245/255, 5/255, 237/255
                if (self.ids[f'p2{i}'].pos_hint == {"center_x": self.w_f_se[0], "center_y": self.w_f_se[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.e_f_se[0], "center_y": self.e_f_se[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.s_f_se[0], "center_y": self.s_f_se[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.n_f_se[0], "center_y": self.n_f_se[1]}) and self.ids[f'p2{i}'].text_color == [0,0.2,0.21,0.31] and self.ids[f'p2{i}'].icon == "record-circle":
                    self.ids[f'p2{i}'].text_color = 245/255, 5/255, 237/255
            for i in range(1, 21):
                if (self.ids[f'p1{i}'].pos_hint == {"center_x": self.n_f_se[0], "center_y": self.n_f_se[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.s_f_se[0], "center_y": self.s_f_se[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.e_f_se[0], "center_y": self.e_f_se[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.w_f_se[0], "center_y": self.w_f_se[1]}) and self.ids[f'p1{i}'].icon != "record-circle":
                    if self.ids.common10.pos_hint == {"center_x": self.xw_f_se[0], "center_y": self.xw_f_se[1]} or self.ids.common10.pos_hint == {"center_x": self.xe_f_se[0], "center_y": self.xe_f_se[1]} or self.ids.common10.pos_hint == {"center_x": self.xs_f_se[0], "center_y": self.xs_f_se[1]} or self.ids.common10.pos_hint == {"center_x": self.xn_f_se[0], "center_y": self.xn_f_se[1]}:
                        mid = ((self.ids.common10.pos_hint['center_x'] + pb_co[0])/2 , (self.ids.common10.pos_hint['center_y'] + pb_co[1])/2)
                        for j in range(1, 21):
                            if (self.ids[f'p2{j}'].pos_hint == {"center_x": self.w_f_se[0], "center_y": self.w_f_se[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.e_f_se[0], "center_y": self.e_f_se[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.s_f_se[0], "center_y": self.s_f_se[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.n_f_se[0], "center_y": self.n_f_se[1]}) and self.ids[f'p2{i}'].icon == "account":
                                if self.ids[f'p2{j}'].pos_hint == {'center_x': mid[0], 'center_y': mid[1]}:
                                    self.ids.common10.text_color = 0,0.2,0.21,0.31  
                        for j in range(1, 21):
                            if (self.ids[f'p1{j}'].pos_hint == {"center_x": self.w_f_se[0], "center_y": self.w_f_se[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.e_f_se[0], "center_y": self.e_f_se[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.s_f_se[0], "center_y": self.s_f_se[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.n_f_se[0], "center_y": self.n_f_se[1]}) and self.ids[f'p1{i}'].icon == "account":
                                if self.ids[f'p1{j}'].pos_hint == {'center_x': mid[0], 'center_y': mid[1]}:
                                    self.ids.common10.text_color = 245/255, 5/255, 237/255
                    for i in range(1, 21):
                        if (self.ids[f'p2{i}'].pos_hint == {"center_x": self.xn_f_se[0], "center_y": self.xn_f_se[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.xw_f_se[0], "center_y": self.xw_f_se[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.xs_f_se[0], "center_y": self.xs_f_se[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.xe_f_se[0], "center_y": self.xe_f_se[1]}) and self.ids[f'p2{i}'].text_color == [0,0.2,0.21,0.31] and self.ids[f'p2{i}'].icon == "record-circle":
                            midp21 = ((self.ids[f'p2{i}'].pos_hint['center_x'] + pb_co[0])/2, (self.ids[f'p2{i}'].pos_hint['center_y'] + pb_co[1])/2)
                            for j in range(1, 21):
                                if (self.ids[f'p2{j}'].pos_hint == {"center_x": self.w_f_se[0], "center_y": self.w_f_se[1]} or self.ids[f'p2{j}'].pos_hint == {"center_x": self.e_f_se[0], "center_y": self.e_f_se[1]} or self.ids[f'p2{j}'].pos_hint == {"center_x": self.s_f_se[0], "center_y": self.s_f_se[1]} or self.ids[f'p2{j}'].pos_hint == {"center_x": self.n_f_se[0], "center_y": self.n_f_se[1]}) and self.ids[f'p2{j}'].icon == "account":
                                    if self.ids[f'p2{j}'].pos_hint == {'center_x': midp21[0], 'center_y': midp21[1]}:
                                        self.ids[f'p2{i}'].text_color = 0,0.2,0.21,0.31   
                        if (self.ids[f'p1{i}'].pos_hint == {"center_x": self.xn_f_se[0], "center_y": self.xn_f_se[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.xw_f_se[0], "center_y": self.xw_f_se[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.xs_f_se[0], "center_y": self.xs_f_se[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.xe_f_se[0], "center_y": self.xe_f_se[1]}) and self.ids[f'p1{i}'].text_color == [0,0.2,0.21,0.31] and self.ids[f'p1{i}'].icon == "record-circle":
                            midp211 = ((self.ids[f'p1{i}'].pos_hint['center_x'] + pb_co[0])/2, (self.ids[f'p1{i}'].pos_hint['center_y'] + pb_co[1])/2)
                            for j in range(1, 21):
                                if (self.ids[f'p2{j}'].pos_hint == {"center_x": self.w_f_se[0], "center_y": self.w_f_se[1]} or self.ids[f'p2{j}'].pos_hint == {"center_x": self.e_f_se[0], "center_y": self.e_f_se[1]} or self.ids[f'p2{j}'].pos_hint == {"center_x": self.s_f_se[0], "center_y": self.s_f_se[1]} or self.ids[f'p2{j}'].pos_hint == {"center_x": self.n_f_se[0], "center_y": self.n_f_se[1]}) and self.ids[f'p2{j}'].icon == "account":
                                    if self.ids[f'p2{j}'].pos_hint == {'center_x': midp211[0], 'center_y': midp211[1]}:
                                        self.ids[f'p1{i}'].text_color = 0,0.2,0.21,0.31   
                    for i in range(1, 21):
                        if (self.ids[f'p2{i}'].pos_hint == {"center_x": self.xn_f_se[0], "center_y": self.xn_f_se[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.xw_f_se[0], "center_y": self.xw_f_se[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.xs_f_se[0], "center_y": self.xs_f_se[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.xe_f_se[0], "center_y": self.xe_f_se[1]}) and self.ids[f'p2{i}'].text_color == [0,0.2,0.21,0.31] and self.ids[f'p2{i}'].icon == "record-circle":
                            midp31 = ((self.ids[f'p2{i}'].pos_hint['center_x'] + pb_co[0])/2, (self.ids[f'p2{i}'].pos_hint['center_y'] + pb_co[1])/2)
                            for j in range(1, 21):
                                if (self.ids[f'p1{j}'].pos_hint == {"center_x": self.w_f_se[0], "center_y": self.w_f_se[1]} or self.ids[f'p1{j}'].pos_hint == {"center_x": self.e_f_se[0], "center_y": self.e_f_se[1]} or self.ids[f'p1{j}'].pos_hint == {"center_x": self.s_f_se[0], "center_y": self.s_f_se[1]} or self.ids[f'p1{j}'].pos_hint == {"center_x": self.n_f_se[0], "center_y": self.n_f_se[1]}) and self.ids[f'p1{j}'].icon == "account":
                                    if self.ids[f'p1{j}'].pos_hint == {'center_x': midp31[0], 'center_y': midp31[1]}:
                                        self.ids[f'p2{i}'].text_color = 245/255, 5/255, 237/255
                        if (self.ids[f'p1{i}'].pos_hint == {"center_x": self.xn_f_se[0], "center_y": self.xn_f_se[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.xw_f_se[0], "center_y": self.xw_f_se[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.xs_f_se[0], "center_y": self.xs_f_se[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.xe_f_se[0], "center_y": self.xe_f_se[1]}) and self.ids[f'p1{i}'].text_color == [0,0.2,0.21,0.31] and self.ids[f'p1{i}'].icon == "record-circle":
                            midp311 = ((self.ids[f'p1{i}'].pos_hint['center_x'] + pb_co[0])/2, (self.ids[f'p1{i}'].pos_hint['center_y'] + pb_co[1])/2)
                            for j in range(1, 21):
                                if (self.ids[f'p1{j}'].pos_hint == {"center_x": self.w_f_se[0], "center_y": self.w_f_se[1]} or self.ids[f'p1{j}'].pos_hint == {"center_x": self.e_f_se[0], "center_y": self.e_f_se[1]} or self.ids[f'p1{j}'].pos_hint == {"center_x": self.s_f_se[0], "center_y": self.s_f_se[1]} or self.ids[f'p1{j}'].pos_hint == {"center_x": self.n_f_se[0], "center_y": self.n_f_se[1]}) and self.ids[f'p1{j}'].icon == "account":
                                    if self.ids[f'p1{j}'].pos_hint == {'center_x': midp311[0], 'center_y': midp311[1]}:
                                        self.ids[f'p1{i}'].text_color = 245/255, 5/255, 237/255   


                                
        elif pb_co == (x,2*y) or pb_co == (3*x, 2*y):
            self.w_f_se = (pb_co[0] - x, pb_co[1])
            self.e_f_se = (pb_co[0]+x, pb_co[1])
            self.n_f_se = (pb_co[0], pb_co[1]+y)
            self.s_f_se = (pb_co[0], pb_co[1]-y)
            self.xw_f_se = (pb_co[0] - 2*x, pb_co[1])
            self.xe_f_se = (pb_co[0]+2*x, pb_co[1])
            self.xn_f_se = (pb_co[0], pb_co[1]+2*y)
            self.xs_f_se = (pb_co[0], pb_co[1]-2*y)
            if self.ids.common10.pos_hint == {"center_x": self.w_f_se[0], "center_y": self.w_f_se[1]} or self.ids.common10.pos_hint == {"center_x": self.e_f_se[0], "center_y": self.e_f_se[1]} or self.ids.common10.pos_hint == {"center_x": self.n_f_se[0], "center_y": self.n_f_se[1]}:
                self.ids.common10.text_color = 245/255, 5/255, 237/255
            for i in range(1, 21):
                if (self.ids[f'p2{i}'].pos_hint == {"center_x": self.w_f_se[0], "center_y": self.w_f_se[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.e_f_se[0], "center_y": self.e_f_se[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.n_f_se[0], "center_y": self.n_f_se[1]}) and self.ids[f'p2{i}'].text_color == [0,0.2,0.21,0.31] and self.ids[f'p2{i}'].icon == "record-circle":
                    self.ids[f'p2{i}'].text_color = 245/255, 5/255, 237/255                
                if (self.ids[f'p1{i}'].pos_hint == {"center_x": self.w_f_se[0], "center_y": self.w_f_se[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.e_f_se[0], "center_y": self.e_f_se[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.n_f_se[0], "center_y": self.n_f_se[1]}) and self.ids[f'p1{i}'].text_color == [0,0.2,0.21,0.31] and self.ids[f'p1{i}'].icon == "record-circle":
                    self.ids[f'p1{i}'].text_color = 245/255, 5/255, 237/255
            for i in range(1, 21):
                if (self.ids[f'p1{i}'].pos_hint == {"center_x": self.w_f_se[0], "center_y": self.w_f_se[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.e_f_se[0], "center_y": self.e_f_se[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.n_f_se[0], "center_y": self.n_f_se[1]}) and self.ids[f'p1{i}'].icon != "record-circle":
                    if self.ids.common10.pos_hint == {"center_x": self.xw_f_se[0], "center_y": self.xw_f_se[1]} or self.ids.common10.pos_hint == {"center_x": self.xe_f_se[0], "center_y": self.xe_f_se[1]} or self.ids.common10.pos_hint == {"center_x": self.xn_f_se[0], "center_y": self.xn_f_se[1]}:
                        mid = ((self.ids.common10.pos_hint['center_x'] + pb_co[0])/2 , (self.ids.common10.pos_hint['center_y'] + pb_co[1])/2)
                        for j in range(1, 21):
                            if (self.ids[f'p2{j}'].pos_hint == {"center_x": self.w_f_se[0], "center_y": self.w_f_se[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.e_f_se[0], "center_y": self.e_f_se[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.n_f_se[0], "center_y": self.n_f_se[1]}) and self.ids[f'p2{i}'].icon == "account":
                                if self.ids[f'p2{j}'].pos_hint == {'center_x': mid[0], 'center_y': mid[1]}:
                                    self.ids.common10.text_color = 0,0.2,0.21,0.31  
                        for j in range(1, 21):
                            if (self.ids[f'p1{j}'].pos_hint == {"center_x": self.w_f_se[0], "center_y": self.w_f_se[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.e_f_se[0], "center_y": self.e_f_se[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.n_f_se[0], "center_y": self.n_f_se[1]}) and self.ids[f'p1{i}'].icon == "account":
                                if self.ids[f'p1{j}'].pos_hint == {'center_x': mid[0], 'center_y': mid[1]}:
                                    self.ids.common10.text_color = 245/255, 5/255, 237/255
                          
                    for i in range(1, 21):
                        if (self.ids[f'p2{i}'].pos_hint == {"center_x": self.xn_f_se[0], "center_y": self.xn_f_se[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.xw_f_se[0], "center_y": self.xw_f_se[1]}  or self.ids[f'p2{i}'].pos_hint == {"center_x": self.xe_f_se[0], "center_y": self.xe_f_se[1]}) and self.ids[f'p2{i}'].text_color == [0,0.2,0.21,0.31] and self.ids[f'p2{i}'].icon == "record-circle":
                            midp1 = ((self.ids[f'p2{i}'].pos_hint['center_x'] + pb_co[0])/2, (self.ids[f'p2{i}'].pos_hint['center_y'] + pb_co[1])/2)
                            for j in range(1, 21):
                                if (self.ids[f'p2{j}'].pos_hint == {"center_x": self.w_f_se[0], "center_y": self.w_f_se[1]} or self.ids[f'p2{j}'].pos_hint == {"center_x": self.e_f_se[0], "center_y": self.e_f_se[1]}  or self.ids[f'p2{j}'].pos_hint == {"center_x": self.n_f_se[0], "center_y": self.n_f_se[1]}) and self.ids[f'p2{j}'].icon == "account":
                                    if self.ids[f'p2{j}'].pos_hint == {'center_x': midp1[0], 'center_y': midp1[1]}:
                                        self.ids[f'p2{i}'].text_color = 0,0.2,0.21,0.31  
                        if (self.ids[f'p1{i}'].pos_hint == {"center_x": self.xw_f_se[0], "center_y": self.xw_f_se[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.xe_f_se[0], "center_y": self.xe_f_se[1]}  or self.ids[f'p1{i}'].pos_hint == {"center_x": self.xn_f_se[0], "center_y": self.xn_f_se[1]}) and self.ids[f'p1{i}'].text_color == [0,0.2,0.21,0.31] and self.ids[f'p1{i}'].icon == "record-circle":
                            midp11 = ((self.ids[f'p1{i}'].pos_hint['center_x'] + pb_co[0])/2, (self.ids[f'p1{i}'].pos_hint['center_y'] + pb_co[1])/2)
                            for j in range(1, 21):
                                if (self.ids[f'p2{j}'].pos_hint == {"center_x": self.w_f_se[0], "center_y": self.w_f_se[1]} or self.ids[f'p2{j}'].pos_hint == {"center_x": self.e_f_se[0], "center_y": self.e_f_se[1]}  or self.ids[f'p2{j}'].pos_hint == {"center_x": self.n_f_se[0], "center_y": self.n_f_se[1]}) and self.ids[f'p2{j}'].icon == "account":
                                    if self.ids[f'p2{j}'].pos_hint == {'center_x': midp11[0], 'center_y': midp11[1]}:
                                        self.ids[f'p1{i}'].text_color = 0,0.2,0.21,0.31  
                    for i in range(1, 21):
                        if (self.ids[f'p2{i}'].pos_hint == {"center_x": self.xn_f_se[0], "center_y": self.xn_f_se[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.xw_f_se[0], "center_y": self.xw_f_se[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.xe_f_se[0], "center_y": self.xe_f_se[1]}) and self.ids[f'p2{i}'].text_color == [0,0.2,0.21,0.31] and self.ids[f'p2{i}'].icon == "record-circle":
                            midp1 = ((self.ids[f'p2{i}'].pos_hint['center_x'] + pb_co[0])/2, (self.ids[f'p2{i}'].pos_hint['center_y'] + pb_co[1])/2)
                            for j in range(1, 21):
                                if (self.ids[f'p1{j}'].pos_hint == {"center_x": self.w_f_se[0], "center_y": self.w_f_se[1]} or self.ids[f'p1{j}'].pos_hint == {"center_x": self.e_f_se[0], "center_y": self.e_f_se[1]}  or self.ids[f'p1{j}'].pos_hint == {"center_x": self.n_f_se[0], "center_y": self.n_f_se[1]}) and self.ids[f'p1{j}'].icon == "account":
                                    if self.ids[f'p1{j}'].pos_hint == {'center_x': midp1[0], 'center_y': midp1[1]}:
                                        self.ids[f'p2{i}'].text_color = 245/255, 5/255, 237/255  
                        if (self.ids[f'p1{i}'].pos_hint == {"center_x": self.xw_f_se[0], "center_y": self.xw_f_se[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.xe_f_se[0], "center_y": self.xe_f_se[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.xn_f_se[0], "center_y": self.xn_f_se[1]}) and self.ids[f'p1{i}'].text_color == [0,0.2,0.21,0.31] and self.ids[f'p1{i}'].icon == "record-circle":
                            midp11 = ((self.ids[f'p1{i}'].pos_hint['center_x'] + pb_co[0])/2, (self.ids[f'p1{i}'].pos_hint['center_y'] + pb_co[1])/2)
                            for j in range(1, 21):
                                if (self.ids[f'p1{j}'].pos_hint == {"center_x": self.w_f_se[0], "center_y": self.w_f_se[1]} or self.ids[f'p1{j}'].pos_hint == {"center_x": self.e_f_se[0], "center_y": self.e_f_se[1]}  or self.ids[f'p1{j}'].pos_hint == {"center_x": self.n_f_se[0], "center_y": self.n_f_se[1]}) and self.ids[f'p1{j}'].icon == "account":
                                    if self.ids[f'p1{j}'].pos_hint == {'center_x': midp11[0], 'center_y': midp11[1]}:
                                        self.ids[f'p1{i}'].text_color = 245/255, 5/255, 237/255
        elif pb_co == (x,6*y) or pb_co == (3*x, 6*y):
            self.w_f_se = (pb_co[0] - x, pb_co[1])
            self.e_f_se = (pb_co[0]+x, pb_co[1])
            self.s_f_se = (pb_co[0], pb_co[1]-y)
            self.xw_f_se = (pb_co[0] - 2*x, pb_co[1])
            self.xe_f_se = (pb_co[0]+2*x, pb_co[1])
            self.xs_f_se = (pb_co[0], pb_co[1]-2*y)
            if self.ids.common10.pos_hint == {"center_x": self.w_f_se[0], "center_y": self.w_f_se[1]} or self.ids.common10.pos_hint == {"center_x": self.e_f_se[0], "center_y": self.e_f_se[1]} or self.ids.common10.pos_hint == {"center_x": self.s_f_se[0], "center_y": self.s_f_se[1]}:
                self.ids.common10.text_color = 245/255, 5/255, 237/255
            for i in range(1, 21):
                if (self.ids[f'p2{i}'].pos_hint == {"center_x": self.w_f_se[0], "center_y": self.w_f_se[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.e_f_se[0], "center_y": self.e_f_se[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.s_f_se[0], "center_y": self.s_f_se[1]}) and self.ids[f'p2{i}'].text_color == [0,0.2,0.21,0.31] and self.ids[f'p2{i}'].icon == "record-circle":
                    self.ids[f'p2{i}'].text_color = 245/255, 5/255, 237/255                
                if (self.ids[f'p1{i}'].pos_hint == {"center_x": self.w_f_se[0], "center_y": self.w_f_se[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.e_f_se[0], "center_y": self.e_f_se[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.s_f_se[0], "center_y": self.s_f_se[1]}) and self.ids[f'p1{i}'].text_color == [0,0.2,0.21,0.31] and self.ids[f'p1{i}'].icon == "record-circle":
                    self.ids[f'p1{i}'].text_color = 245/255, 5/255, 237/255
            for i in range(1, 21):
                if (self.ids[f'p1{i}'].pos_hint == {"center_x": self.w_f_se[0], "center_y": self.w_f_se[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.e_f_se[0], "center_y": self.e_f_se[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.s_f_se[0], "center_y": self.s_f_se[1]}) and self.ids[f'p1{i}'].icon != "record-circle":
                    if self.ids.common10.pos_hint == {"center_x": self.xw_f_se[0], "center_y": self.xw_f_se[1]} or self.ids.common10.pos_hint == {"center_x": self.xe_f_se[0], "center_y": self.xe_f_se[1]} or self.ids.common10.pos_hint == {"center_x": self.xs_f_se[0], "center_y": self.xs_f_se[1]}:
                        mid = ((self.ids.common10.pos_hint['center_x'] + pb_co[0])/2 , (self.ids.common10.pos_hint['center_y'] + pb_co[1])/2)
                        for j in range(1, 21):
                            if (self.ids[f'p2{j}'].pos_hint == {"center_x": self.w_f_se[0], "center_y": self.w_f_se[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.e_f_se[0], "center_y": self.e_f_se[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.s_f_se[0], "center_y": self.s_f_se[1]}) and self.ids[f'p2{i}'].icon == "account":
                                if self.ids[f'p2{j}'].pos_hint == {'center_x': mid[0], 'center_y': mid[1]}:
                                    self.ids.common10.text_color = 0,0.2,0.21,0.31  
                        for j in range(1, 21):
                            if (self.ids[f'p1{j}'].pos_hint == {"center_x": self.w_f_se[0], "center_y": self.w_f_se[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.e_f_se[0], "center_y": self.e_f_se[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.s_f_se[0], "center_y": self.s_f_se[1]}) and self.ids[f'p1{i}'].icon == "account":
                                if self.ids[f'p1{j}'].pos_hint == {'center_x': mid[0], 'center_y': mid[1]}:
                                    self.ids.common10.text_color = 245/255, 5/255, 237/255
                          
                    for i in range(1, 21):
                        if (self.ids[f'p2{i}'].pos_hint == {"center_x": self.xs_f_se[0], "center_y": self.xs_f_se[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.xw_f_se[0], "center_y": self.xw_f_se[1]}  or self.ids[f'p2{i}'].pos_hint == {"center_x": self.xe_f_se[0], "center_y": self.xe_f_se[1]}) and self.ids[f'p2{i}'].text_color == [0,0.2,0.21,0.31] and self.ids[f'p2{i}'].icon == "record-circle":
                            midp1 = ((self.ids[f'p2{i}'].pos_hint['center_x'] + pb_co[0])/2, (self.ids[f'p2{i}'].pos_hint['center_y'] + pb_co[1])/2)
                            for j in range(1, 21):
                                if (self.ids[f'p2{j}'].pos_hint == {"center_x": self.w_f_se[0], "center_y": self.w_f_se[1]} or self.ids[f'p2{j}'].pos_hint == {"center_x": self.e_f_se[0], "center_y": self.e_f_se[1]}  or self.ids[f'p2{j}'].pos_hint == {"center_x": self.s_f_se[0], "center_y": self.s_f_se[1]}) and self.ids[f'p2{j}'].icon == "account":
                                    if self.ids[f'p2{j}'].pos_hint == {'center_x': midp1[0], 'center_y': midp1[1]}:
                                        self.ids[f'p2{i}'].text_color = 0,0.2,0.21,0.31  
                        if (self.ids[f'p1{i}'].pos_hint == {"center_x": self.xw_f_se[0], "center_y": self.xw_f_se[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.xe_f_se[0], "center_y": self.xe_f_se[1]}  or self.ids[f'p1{i}'].pos_hint == {"center_x": self.xs_f_se[0], "center_y": self.xs_f_se[1]}) and self.ids[f'p1{i}'].text_color == [0,0.2,0.21,0.31] and self.ids[f'p1{i}'].icon == "record-circle":
                            midp11 = ((self.ids[f'p1{i}'].pos_hint['center_x'] + pb_co[0])/2, (self.ids[f'p1{i}'].pos_hint['center_y'] + pb_co[1])/2)
                            for j in range(1, 21):
                                if (self.ids[f'p2{j}'].pos_hint == {"center_x": self.w_f_se[0], "center_y": self.w_f_se[1]} or self.ids[f'p2{j}'].pos_hint == {"center_x": self.e_f_se[0], "center_y": self.e_f_se[1]}  or self.ids[f'p2{j}'].pos_hint == {"center_x": self.s_f_se[0], "center_y": self.s_f_se[1]}) and self.ids[f'p2{j}'].icon == "account":
                                    if self.ids[f'p2{j}'].pos_hint == {'center_x': midp11[0], 'center_y': midp11[1]}:
                                        self.ids[f'p1{i}'].text_color = 0,0.2,0.21,0.31  
                    for i in range(1, 21):
                        if (self.ids[f'p2{i}'].pos_hint == {"center_x": self.xs_f_se[0], "center_y": self.xs_f_se[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.xw_f_se[0], "center_y": self.xw_f_se[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.xe_f_se[0], "center_y": self.xe_f_se[1]}) and self.ids[f'p2{i}'].text_color == [0,0.2,0.21,0.31] and self.ids[f'p2{i}'].icon == "record-circle":
                            midp1 = ((self.ids[f'p2{i}'].pos_hint['center_x'] + pb_co[0])/2, (self.ids[f'p2{i}'].pos_hint['center_y'] + pb_co[1])/2)
                            for j in range(1, 21):
                                if (self.ids[f'p1{j}'].pos_hint == {"center_x": self.w_f_se[0], "center_y": self.w_f_se[1]} or self.ids[f'p1{j}'].pos_hint == {"center_x": self.e_f_se[0], "center_y": self.e_f_se[1]}  or self.ids[f'p1{j}'].pos_hint == {"center_x": self.s_f_se[0], "center_y": self.s_f_se[1]}) and self.ids[f'p1{j}'].icon == "account":
                                    if self.ids[f'p1{j}'].pos_hint == {'center_x': midp1[0], 'center_y': midp1[1]}:
                                        self.ids[f'p2{i}'].text_color = 245/255, 5/255, 237/255  
                        if (self.ids[f'p1{i}'].pos_hint == {"center_x": self.xw_f_se[0], "center_y": self.xw_f_se[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.xe_f_se[0], "center_y": self.xe_f_se[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.xs_f_se[0], "center_y": self.xs_f_se[1]}) and self.ids[f'p1{i}'].text_color == [0,0.2,0.21,0.31] and self.ids[f'p1{i}'].icon == "record-circle":
                            midp11 = ((self.ids[f'p1{i}'].pos_hint['center_x'] + pb_co[0])/2, (self.ids[f'p1{i}'].pos_hint['center_y'] + pb_co[1])/2)
                            for j in range(1, 21):
                                if (self.ids[f'p1{j}'].pos_hint == {"center_x": self.w_f_se[0], "center_y": self.w_f_se[1]} or self.ids[f'p1{j}'].pos_hint == {"center_x": self.e_f_se[0], "center_y": self.e_f_se[1]}  or self.ids[f'p1{j}'].pos_hint == {"center_x": self.s_f_se[0], "center_y": self.s_f_se[1]}) and self.ids[f'p1{j}'].icon == "account":
                                    if self.ids[f'p1{j}'].pos_hint == {'center_x': midp11[0], 'center_y': midp11[1]}:
                                        self.ids[f'p1{i}'].text_color = 245/255, 5/255, 237/255   
        elif pb_co == (x,y):
            self.e_f_se = (pb_co[0]+x, pb_co[1])
            self.s_f_se = (pb_co[0], pb_co[1]-y)
            self.ne_f_se = (pb_co[0] + x, pb_co[1] + y)
            self.sw_f_se = (pb_co[0] - x, pb_co[1] - y)
            self.se_f_se = (pb_co[0] + x, pb_co[1] - y)
            self.xe_f_se = (pb_co[0]+ 2*x, pb_co[1])
            self.xne_f_se = (pb_co[0] + 2*x, pb_co[1] + 2*y)
            if self.ids.common10.pos_hint == {"center_x": self.e_f_se[0], "center_y": self.e_f_se[1]} or self.ids.common10.pos_hint == {"center_x": self.s_f_se[0], "center_y": self.s_f_se[1]}or  self.ids.common10.pos_hint == {"center_x": self.sw_f_se[0], "center_y": self.sw_f_se[1]} or self.ids.common10.pos_hint == {"center_x": self.se_f_se[0], "center_y": self.se_f_se[1]}  or self.ids.common10.pos_hint == {"center_x": self.ne_f_se[0], "center_y": self.ne_f_se[1]}:
                self.ids.common10.text_color = 245/255, 5/255, 237/255
            for i in range(1, 21):
                if (self.ids[f'p2{i}'].pos_hint == {"center_x": self.e_f_se[0], "center_y": self.e_f_se[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.s_f_se[0], "center_y": self.s_f_se[1]}  or self.ids[f'p2{i}'].pos_hint == {"center_x": self.sw_f_se[0], "center_y": self.sw_f_se[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.se_f_se[0], "center_y": self.se_f_se[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.ne_f_se[0], "center_y": self.ne_f_se[1]}) and self.ids[f'p2{i}'].icon == "record-circle" and self.ids[f'p2{i}'].text_color == [0,0.2,0.21,0.31]:
                    self.ids[f'p2{i}'].text_color = 245/255, 5/255, 237/255
                if (self.ids[f'p1{i}'].pos_hint == {"center_x": self.e_f_se[0], "center_y": self.e_f_se[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.s_f_se[0], "center_y": self.s_f_se[1]}  or self.ids[f'p1{i}'].pos_hint == {"center_x": self.sw_f_se[0], "center_y": self.sw_f_se[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.se_f_se[0], "center_y": self.se_f_se[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.ne_f_se[0], "center_y": self.ne_f_se[1]}) and self.ids[f'p1{i}'].icon == "record-circle" and self.ids[f'p1{i}'].text_color == [0,0.2,0.21,0.31]:
                    self.ids[f'p1{i}'].text_color = 245/255, 5/255, 237/255
            for i in range(1, 21):
                if (self.ids[f'p1{i}'].pos_hint == {"center_x": self.e_f_se[0], "center_y": self.e_f_se[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.ne_f_se[0], "center_y": self.ne_f_se[1]}) and self.ids[f'p1{i}'].icon != "record-circle":
                    if self.ids.common10.pos_hint == {"center_x": self.xe_f_se[0], "center_y": self.xe_f_se[1]} or self.ids.common10.pos_hint == {"center_x": self.xne_f_se[0], "center_y": self.xne_f_se[1]}:
                        mid = ((self.ids.common10.pos_hint['center_x'] + pb_co[0])/2 , (self.ids.common10.pos_hint['center_y'] + pb_co[1])/2)
                        for j in range(1, 21):
                            if (self.ids[f'p2{j}'].pos_hint == {"center_x": self.e_f_se[0], "center_y": self.e_f_se[1]} or self.ids[f'p2{j}'].pos_hint == {"center_x": self.ne_f_se[0], "center_y": self.ne_f_se[1]}) and self.ids[f'p2{j}'].icon == "account":
                                if self.ids[f'p2{j}'].pos_hint == {'center_x': mid[0], 'center_y': mid[1]}:
                                    self.ids.common10.text_color = 0,0.2,0.21,0.31  
                        for j in range(1, 21):
                            if (self.ids[f'p1{j}'].pos_hint == {"center_x": self.e_f_se[0], "center_y": self.e_f_se[1]} or self.ids[f'p1{j}'].pos_hint == {"center_x": self.ne_f_se[0], "center_y": self.ne_f_se[1]}) and self.ids[f'p1{j}'].icon == "account":
                                if self.ids[f'p1{j}'].pos_hint == {'center_x': mid[0], 'center_y': mid[1]}:
                                    self.ids.common10.text_color = 245/255, 5/255, 237/255 
                    for i in range(1, 21):
                        if (self.ids[f'p2{i}'].pos_hint == {"center_x": self.xe_f_se[0], "center_y": self.xe_f_se[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.xne_f_se[0], "center_y": self.xne_f_se[1]}) and self.ids[f'p2{i}'].text_color == [0,0.2,0.21,0.31] and self.ids[f'p2{i}'].icon == "record-circle":
                            midp1 = ((self.ids[f'p2{i}'].pos_hint['center_x'] + pb_co[0])/2, (self.ids[f'p2{i}'].pos_hint['center_y'] + pb_co[1])/2)
                            for j in range(1, 21):
                                if (self.ids[f'p2{j}'].pos_hint == {"center_x": self.e_f_se[0], "center_y": self.e_f_se[1]} or self.ids[f'p2{j}'].pos_hint == {"center_x": self.ne_f_se[0], "center_y": self.ne_f_se[1]}) and self.ids[f'p2{j}'].icon == "account":
                                    if self.ids[f'p2{j}'].pos_hint == {'center_x': midp1[0], 'center_y': midp1[1]}:
                                        self.ids[f'p2{i}'].text_color = 0,0.2,0.21,0.31   
                        if (self.ids[f'p1{i}'].pos_hint == {"center_x": self.xe_f_se[0], "center_y": self.xe_f_se[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.xne_f_se[0], "center_y": self.xne_f_se[1]}) and self.ids[f'p1{i}'].text_color == [0,0.2,0.21,0.31] and self.ids[f'p1{i}'].icon == "record-circle":
                            midp11 = ((self.ids[f'p1{i}'].pos_hint['center_x'] + pb_co[0])/2, (self.ids[f'p1{i}'].pos_hint['center_y'] + pb_co[1])/2)
                            for j in range(1, 21):
                                if (self.ids[f'p2{j}'].pos_hint == {"center_x": self.e_f_se[0], "center_y": self.e_f_se[1]} or self.ids[f'p2{j}'].pos_hint == {"center_x": self.ne_f_se[0], "center_y": self.ne_f_se[1]}) and self.ids[f'p2{j}'].icon == "account":
                                    if self.ids[f'p2{j}'].pos_hint == {'center_x': midp11[0], 'center_y': midp11[1]}:
                                        self.ids[f'p1{i}'].text_color = 0,0.2,0.21,0.31   
                    for i in range(1, 21):
                        if (self.ids[f'p2{i}'].pos_hint == {"center_x": self.xe_f_se[0], "center_y": self.xe_f_se[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.xne_f_se[0], "center_y": self.xne_f_se[1]}) and self.ids[f'p2{i}'].text_color == [0,0.2,0.21,0.31] and self.ids[f'p2{i}'].icon == "record-circle":
                            midp1 = ((self.ids[f'p2{i}'].pos_hint['center_x'] + pb_co[0])/2, (self.ids[f'p2{i}'].pos_hint['center_y'] + pb_co[1])/2)
                            for j in range(1, 21):
                                if (self.ids[f'p1{j}'].pos_hint == {"center_x": self.e_f_se[0], "center_y": self.e_f_se[1]} or self.ids[f'p1{j}'].pos_hint == {"center_x": self.ne_f_se[0], "center_y": self.ne_f_se[1]}) and self.ids[f'p1{j}'].icon == "account":
                                    if self.ids[f'p1{j}'].pos_hint == {'center_x': midp1[0], 'center_y': midp1[1]}:
                                        self.ids[f'p2{i}'].text_color = 245/255, 5/255, 237/255
                        if (self.ids[f'p1{i}'].pos_hint == {"center_x": self.xe_f_se[0], "center_y": self.xe_f_se[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.xne_f_se[0], "center_y": self.xne_f_se[1]}) and self.ids[f'p1{i}'].text_color == [0,0.2,0.21,0.31] and self.ids[f'p1{i}'].icon == "record-circle":
                            midp11 = ((self.ids[f'p1{i}'].pos_hint['center_x'] + pb_co[0])/2, (self.ids[f'p1{i}'].pos_hint['center_y'] + pb_co[1])/2)
                            for j in range(1, 21):
                                if (self.ids[f'p1{j}'].pos_hint == {"center_x": self.e_f_se[0], "center_y": self.e_f_se[1]} or self.ids[f'p1{j}'].pos_hint == {"center_x": self.ne_f_se[0], "center_y": self.ne_f_se[1]}) and self.ids[f'p1{j}'].icon == "account":
                                    if self.ids[f'p1{j}'].pos_hint == {'center_x': midp11[0], 'center_y': midp11[1]}:
                                        self.ids[f'p1{i}'].text_color = 245/255, 5/255, 237/255  
        elif pb_co == (3*x,y):
            self.w_f_se = (pb_co[0] - x, pb_co[1])
            self.s_f_se = (pb_co[0], pb_co[1]-y)
            self.nw_f_se = (pb_co[0] - x, pb_co[1] + y)
            self.sw_f_se = (pb_co[0] - x, pb_co[1] - y)
            self.se_f_se = (pb_co[0] + x, pb_co[1] - y)
            self.xw_f_se = (pb_co[0] - 2*x, pb_co[1])
            self.xnw_f_se = (pb_co[0] - 2*x, pb_co[1] + 2*y)
            if self.ids.common10.pos_hint == {"center_x": self.w_f_se[0], "center_y": self.w_f_se[1]} or self.ids.common10.pos_hint == {"center_x": self.s_f_se[0], "center_y": self.s_f_se[1]}or  self.ids.common10.pos_hint == {"center_x": self.sw_f_se[0], "center_y": self.sw_f_se[1]} or self.ids.common10.pos_hint == {"center_x": self.se_f_se[0], "center_y": self.se_f_se[1]}  or self.ids.common10.pos_hint == {"center_x": self.nw_f_se[0], "center_y": self.nw_f_se[1]}:
                self.ids.common10.text_color = 245/255, 5/255, 237/255
            for i in range(1, 21):
                if (self.ids[f'p2{i}'].pos_hint == {"center_x": self.w_f_se[0], "center_y": self.w_f_se[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.s_f_se[0], "center_y": self.s_f_se[1]}  or self.ids[f'p2{i}'].pos_hint == {"center_x": self.sw_f_se[0], "center_y": self.sw_f_se[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.se_f_se[0], "center_y": self.se_f_se[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.nw_f_se[0], "center_y": self.nw_f_se[1]}) and self.ids[f'p2{i}'].icon == "record-circle" and self.ids[f'p2{i}'].text_color == [0,0.2,0.21,0.31]:
                    self.ids[f'p2{i}'].text_color = 245/255, 5/255, 237/255
                if (self.ids[f'p1{i}'].pos_hint == {"center_x": self.w_f_se[0], "center_y": self.w_f_se[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.s_f_se[0], "center_y": self.s_f_se[1]}  or self.ids[f'p1{i}'].pos_hint == {"center_x": self.sw_f_se[0], "center_y": self.sw_f_se[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.se_f_se[0], "center_y": self.se_f_se[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.nw_f_se[0], "center_y": self.nw_f_se[1]}) and self.ids[f'p1{i}'].icon == "record-circle" and self.ids[f'p1{i}'].text_color == [0,0.2,0.21,0.31]:
                    self.ids[f'p1{i}'].text_color = 245/255, 5/255, 237/255
            for i in range(1, 21):
                if (self.ids[f'p1{i}'].pos_hint == {"center_x": self.w_f_se[0], "center_y": self.w_f_se[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.nw_f_se[0], "center_y": self.nw_f_se[1]}) and self.ids[f'p1{i}'].icon != "record-circle":
                    if self.ids.common10.pos_hint == {"center_x": self.xw_f_se[0], "center_y": self.xw_f_se[1]} or self.ids.common10.pos_hint == {"center_x": self.xnw_f_se[0], "center_y": self.xnw_f_se[1]}:
                        mid = ((self.ids.common10.pos_hint['center_x'] + pb_co[0])/2 , (self.ids.common10.pos_hint['center_y'] + pb_co[1])/2)
                        for j in range(1, 21):
                            if (self.ids[f'p2{j}'].pos_hint == {"center_x": self.w_f_se[0], "center_y": self.w_f_se[1]} or self.ids[f'p2{j}'].pos_hint == {"center_x": self.nw_f_se[0], "center_y": self.nw_f_se[1]}) and self.ids[f'p2{j}'].icon == "account":
                                if self.ids[f'p2{j}'].pos_hint == {'center_x': mid[0], 'center_y': mid[1]}:
                                    self.ids.common10.text_color = 0,0.2,0.21,0.31  
                        for j in range(1, 21):
                            if (self.ids[f'p1{j}'].pos_hint == {"center_x": self.w_f_se[0], "center_y": self.w_f_se[1]} or self.ids[f'p1{j}'].pos_hint == {"center_x": self.nw_f_se[0], "center_y": self.nw_f_se[1]}) and self.ids[f'p1{j}'].icon == "account":
                                if self.ids[f'p1{j}'].pos_hint == {'center_x': mid[0], 'center_y': mid[1]}:
                                    self.ids.common10.text_color = 245/255, 5/255, 237/255 
                    for i in range(1, 21):
                        if (self.ids[f'p2{i}'].pos_hint == {"center_x": self.xw_f_se[0], "center_y": self.xw_f_se[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.xnw_f_se[0], "center_y": self.xnw_f_se[1]}) and self.ids[f'p2{i}'].text_color == [0,0.2,0.21,0.31] and self.ids[f'p2{i}'].icon == "record-circle":
                            midp1 = ((self.ids[f'p2{i}'].pos_hint['center_x'] + pb_co[0])/2, (self.ids[f'p2{i}'].pos_hint['center_y'] + pb_co[1])/2)
                            for j in range(1, 21):
                                if (self.ids[f'p2{j}'].pos_hint == {"center_x": self.w_f_se[0], "center_y": self.w_f_se[1]} or self.ids[f'p2{j}'].pos_hint == {"center_x": self.nw_f_se[0], "center_y": self.nw_f_se[1]}) and self.ids[f'p2{j}'].icon == "account":
                                    if self.ids[f'p2{j}'].pos_hint == {'center_x': midp1[0], 'center_y': midp1[1]}:
                                        self.ids[f'p2{i}'].text_color = 0,0.2,0.21,0.31   
                        if (self.ids[f'p1{i}'].pos_hint == {"center_x": self.xw_f_se[0], "center_y": self.xw_f_se[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.xnw_f_se[0], "center_y": self.xnw_f_se[1]}) and self.ids[f'p1{i}'].text_color == [0,0.2,0.21,0.31] and self.ids[f'p1{i}'].icon == "record-circle":
                            midp11 = ((self.ids[f'p1{i}'].pos_hint['center_x'] + pb_co[0])/2, (self.ids[f'p1{i}'].pos_hint['center_y'] + pb_co[1])/2)
                            for j in range(1, 21):
                                if (self.ids[f'p2{j}'].pos_hint == {"center_x": self.w_f_se[0], "center_y": self.w_f_se[1]} or self.ids[f'p2{j}'].pos_hint == {"center_x": self.nw_f_se[0], "center_y": self.nw_f_se[1]}) and self.ids[f'p2{j}'].icon == "account":
                                    if self.ids[f'p2{j}'].pos_hint == {'center_x': midp11[0], 'center_y': midp11[1]}:
                                        self.ids[f'p1{i}'].text_color = 0,0.2,0.21,0.31   
                    for i in range(1, 21):
                        if (self.ids[f'p2{i}'].pos_hint == {"center_x": self.xw_f_se[0], "center_y": self.xw_f_se[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.xnw_f_se[0], "center_y": self.xnw_f_se[1]}) and self.ids[f'p2{i}'].text_color == [0,0.2,0.21,0.31] and self.ids[f'p2{i}'].icon == "record-circle":
                            midp1 = ((self.ids[f'p2{i}'].pos_hint['center_x'] + pb_co[0])/2, (self.ids[f'p2{i}'].pos_hint['center_y'] + pb_co[1])/2)
                            for j in range(1, 21):
                                if (self.ids[f'p1{j}'].pos_hint == {"center_x": self.w_f_se[0], "center_y": self.w_f_se[1]} or self.ids[f'p1{j}'].pos_hint == {"center_x": self.nw_f_se[0], "center_y": self.nw_f_se[1]}) and self.ids[f'p1{j}'].icon == "account":
                                    if self.ids[f'p1{j}'].pos_hint == {'center_x': midp1[0], 'center_y': midp1[1]}:
                                        self.ids[f'p2{i}'].text_color = 245/255, 5/255, 237/255
                        if (self.ids[f'p1{i}'].pos_hint == {"center_x": self.xw_f_se[0], "center_y": self.xw_f_se[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.xnw_f_se[0], "center_y": self.xnw_f_se[1]}) and self.ids[f'p1{i}'].text_color == [0,0.2,0.21,0.31] and self.ids[f'p1{i}'].icon == "record-circle":
                            midp11 = ((self.ids[f'p1{i}'].pos_hint['center_x'] + pb_co[0])/2, (self.ids[f'p1{i}'].pos_hint['center_y'] + pb_co[1])/2)
                            for j in range(1, 21):
                                if (self.ids[f'p1{j}'].pos_hint == {"center_x": self.w_f_se[0], "center_y": self.w_f_se[1]} or self.ids[f'p1{j}'].pos_hint == {"center_x": self.nw_f_se[0], "center_y": self.nw_f_se[1]}) and self.ids[f'p1{j}'].icon == "account":
                                    if self.ids[f'p1{j}'].pos_hint == {'center_x': midp11[0], 'center_y': midp11[1]}:
                                        self.ids[f'p1{i}'].text_color = 245/255, 5/255, 237/255  
        elif pb_co == (x,7*y):
            self.e_f_se = (pb_co[0]+x, pb_co[1])
            self.n_f_se = (pb_co[0], pb_co[1]+y)
            self.ne_f_se = (pb_co[0] + x, pb_co[1] + y)
            self.nw_f_se = (pb_co[0] - x, pb_co[1] + y)
            self.se_f_se = (pb_co[0] + x, pb_co[1] - y)
            self.xe_f_se = (pb_co[0]+ 2*x, pb_co[1])
            self.xse_f_se = (pb_co[0] + 2*x, pb_co[1] - 2*y)
            if self.ids.common10.pos_hint == {"center_x": self.e_f_se[0], "center_y": self.e_f_se[1]} or self.ids.common10.pos_hint == {"center_x": self.n_f_se[0], "center_y": self.n_f_se[1]}or  self.ids.common10.pos_hint == {"center_x": self.nw_f_se[0], "center_y": self.nw_f_se[1]} or self.ids.common10.pos_hint == {"center_x": self.se_f_se[0], "center_y": self.se_f_se[1]}  or self.ids.common10.pos_hint == {"center_x": self.ne_f_se[0], "center_y": self.ne_f_se[1]}:
                self.ids.common10.text_color = 245/255, 5/255, 237/255
            for i in range(1, 21):
                if (self.ids[f'p2{i}'].pos_hint == {"center_x": self.e_f_se[0], "center_y": self.e_f_se[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.n_f_se[0], "center_y": self.n_f_se[1]}  or self.ids[f'p2{i}'].pos_hint == {"center_x": self.nw_f_se[0], "center_y": self.nw_f_se[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.se_f_se[0], "center_y": self.se_f_se[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.ne_f_se[0], "center_y": self.ne_f_se[1]}) and self.ids[f'p2{i}'].icon == "record-circle" and self.ids[f'p2{i}'].text_color == [0,0.2,0.21,0.31]:
                    self.ids[f'p2{i}'].text_color = 245/255, 5/255, 237/255
                if (self.ids[f'p1{i}'].pos_hint == {"center_x": self.e_f_se[0], "center_y": self.e_f_se[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.n_f_se[0], "center_y": self.n_f_se[1]}  or self.ids[f'p1{i}'].pos_hint == {"center_x": self.nw_f_se[0], "center_y": self.nw_f_se[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.se_f_se[0], "center_y": self.se_f_se[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.ne_f_se[0], "center_y": self.ne_f_se[1]}) and self.ids[f'p1{i}'].icon == "record-circle" and self.ids[f'p1{i}'].text_color == [0,0.2,0.21,0.31]:
                    self.ids[f'p1{i}'].text_color = 245/255, 5/255, 237/255
            for i in range(1, 21):
                if (self.ids[f'p1{i}'].pos_hint == {"center_x": self.e_f_se[0], "center_y": self.e_f_se[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.se_f_se[0], "center_y": self.se_f_se[1]}) and self.ids[f'p1{i}'].icon != "record-circle":
                    if self.ids.common10.pos_hint == {"center_x": self.xe_f_se[0], "center_y": self.xe_f_se[1]} or self.ids.common10.pos_hint == {"center_x": self.xse_f_se[0], "center_y": self.xse_f_se[1]}:
                        mid = ((self.ids.common10.pos_hint['center_x'] + pb_co[0])/2 , (self.ids.common10.pos_hint['center_y'] + pb_co[1])/2)
                        for j in range(1, 21):
                            if (self.ids[f'p2{j}'].pos_hint == {"center_x": self.e_f_se[0], "center_y": self.e_f_se[1]} or self.ids[f'p2{j}'].pos_hint == {"center_x": self.se_f_se[0], "center_y": self.se_f_se[1]}) and self.ids[f'p2{j}'].icon == "account":
                                if self.ids[f'p2{j}'].pos_hint == {'center_x': mid[0], 'center_y': mid[1]}:
                                    self.ids.common10.text_color = 0,0.2,0.21,0.31  
                        for j in range(1, 21):
                            if (self.ids[f'p1{j}'].pos_hint == {"center_x": self.e_f_se[0], "center_y": self.e_f_se[1]} or self.ids[f'p1{j}'].pos_hint == {"center_x": self.se_f_se[0], "center_y": self.se_f_se[1]}) and self.ids[f'p1{j}'].icon == "account":
                                if self.ids[f'p1{j}'].pos_hint == {'center_x': mid[0], 'center_y': mid[1]}:
                                    self.ids.common10.text_color = 245/255, 5/255, 237/255 
                    for i in range(1, 21):
                        if (self.ids[f'p2{i}'].pos_hint == {"center_x": self.xe_f_se[0], "center_y": self.xe_f_se[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.xse_f_se[0], "center_y": self.xse_f_se[1]}) and self.ids[f'p2{i}'].text_color == [0,0.2,0.21,0.31] and self.ids[f'p2{i}'].icon == "record-circle":
                            midp1 = ((self.ids[f'p2{i}'].pos_hint['center_x'] + pb_co[0])/2, (self.ids[f'p2{i}'].pos_hint['center_y'] + pb_co[1])/2)
                            for j in range(1, 21):
                                if (self.ids[f'p2{j}'].pos_hint == {"center_x": self.e_f_se[0], "center_y": self.e_f_se[1]} or self.ids[f'p2{j}'].pos_hint == {"center_x": self.se_f_se[0], "center_y": self.se_f_se[1]}) and self.ids[f'p2{j}'].icon == "account":
                                    if self.ids[f'p2{j}'].pos_hint == {'center_x': midp1[0], 'center_y': midp1[1]}:
                                        self.ids[f'p2{i}'].text_color = 0,0.2,0.21,0.31   
                        if (self.ids[f'p1{i}'].pos_hint == {"center_x": self.xe_f_se[0], "center_y": self.xe_f_se[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.xse_f_se[0], "center_y": self.xse_f_se[1]}) and self.ids[f'p1{i}'].text_color == [0,0.2,0.21,0.31] and self.ids[f'p1{i}'].icon == "record-circle":
                            midp11 = ((self.ids[f'p1{i}'].pos_hint['center_x'] + pb_co[0])/2, (self.ids[f'p1{i}'].pos_hint['center_y'] + pb_co[1])/2)
                            for j in range(1, 21):
                                if (self.ids[f'p2{j}'].pos_hint == {"center_x": self.e_f_se[0], "center_y": self.e_f_se[1]} or self.ids[f'p2{j}'].pos_hint == {"center_x": self.se_f_se[0], "center_y": self.se_f_se[1]}) and self.ids[f'p2{j}'].icon == "account":
                                    if self.ids[f'p2{j}'].pos_hint == {'center_x': midp11[0], 'center_y': midp11[1]}:
                                        self.ids[f'p1{i}'].text_color = 0,0.2,0.21,0.31   
                    for i in range(1, 21):
                        if (self.ids[f'p2{i}'].pos_hint == {"center_x": self.xe_f_se[0], "center_y": self.xe_f_se[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.xse_f_se[0], "center_y": self.xse_f_se[1]}) and self.ids[f'p2{i}'].text_color == [0,0.2,0.21,0.31] and self.ids[f'p2{i}'].icon == "record-circle":
                            midp1 = ((self.ids[f'p2{i}'].pos_hint['center_x'] + pb_co[0])/2, (self.ids[f'p2{i}'].pos_hint['center_y'] + pb_co[1])/2)
                            for j in range(1, 21):
                                if (self.ids[f'p1{j}'].pos_hint == {"center_x": self.e_f_se[0], "center_y": self.e_f_se[1]} or self.ids[f'p1{j}'].pos_hint == {"center_x": self.se_f_se[0], "center_y": self.se_f_se[1]}) and self.ids[f'p1{j}'].icon == "account":
                                    if self.ids[f'p1{j}'].pos_hint == {'center_x': midp1[0], 'center_y': midp1[1]}:
                                        self.ids[f'p2{i}'].text_color = 245/255, 5/255, 237/255
                        if (self.ids[f'p1{i}'].pos_hint == {"center_x": self.xe_f_se[0], "center_y": self.xe_f_se[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.xse_f_se[0], "center_y": self.xse_f_se[1]}) and self.ids[f'p1{i}'].text_color == [0,0.2,0.21,0.31] and self.ids[f'p1{i}'].icon == "record-circle":
                            midp11 = ((self.ids[f'p1{i}'].pos_hint['center_x'] + pb_co[0])/2, (self.ids[f'p1{i}'].pos_hint['center_y'] + pb_co[1])/2)
                            for j in range(1, 21):
                                if (self.ids[f'p1{j}'].pos_hint == {"center_x": self.e_f_se[0], "center_y": self.e_f_se[1]} or self.ids[f'p1{j}'].pos_hint == {"center_x": self.se_f_se[0], "center_y": self.se_f_se[1]}) and self.ids[f'p1{j}'].icon == "account":
                                    if self.ids[f'p1{j}'].pos_hint == {'center_x': midp11[0], 'center_y': midp11[1]}:
                                        self.ids[f'p1{i}'].text_color = 245/255, 5/255, 237/255  
        elif pb_co == (3*x,7*y):
            self.w_f_se = (pb_co[0] - x, pb_co[1])
            self.n_f_se = (pb_co[0], pb_co[1]+y)
            self.ne_f_se = (pb_co[0] + x, pb_co[1] + y)
            self.nw_f_se = (pb_co[0] - x, pb_co[1] + y)
            self.sw_f_se = (pb_co[0] - x, pb_co[1] - y)
            self.xw_f_se = (pb_co[0] - 2*x, pb_co[1])
            self.xsw_f_se = (pb_co[0] - 2*x, pb_co[1] - 2*y)
            if self.ids.common10.pos_hint == {"center_x": self.w_f_se[0], "center_y": self.w_f_se[1]} or self.ids.common10.pos_hint == {"center_x": self.n_f_se[0], "center_y": self.n_f_se[1]}or  self.ids.common10.pos_hint == {"center_x": self.sw_f_se[0], "center_y": self.sw_f_se[1]} or self.ids.common10.pos_hint == {"center_x": self.ne_f_se[0], "center_y": self.ne_f_se[1]}  or self.ids.common10.pos_hint == {"center_x": self.sw_f_se[0], "center_y": self.sw_f_se[1]}:
                self.ids.common10.text_color = 245/255, 5/255, 237/255
            for i in range(1, 21):
                if (self.ids[f'p2{i}'].pos_hint == {"center_x": self.w_f_se[0], "center_y": self.w_f_se[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.n_f_se[0], "center_y": self.n_f_se[1]}  or self.ids[f'p2{i}'].pos_hint == {"center_x": self.sw_f_se[0], "center_y": self.sw_f_se[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.ne_f_se[0], "center_y": self.ne_f_se[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.sw_f_se[0], "center_y": self.sw_f_se[1]}) and self.ids[f'p2{i}'].icon == "record-circle" and self.ids[f'p2{i}'].text_color == [0,0.2,0.21,0.31]:
                    self.ids[f'p2{i}'].text_color = 245/255, 5/255, 237/255
                if (self.ids[f'p1{i}'].pos_hint == {"center_x": self.w_f_se[0], "center_y": self.w_f_se[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.n_f_se[0], "center_y": self.n_f_se[1]}  or self.ids[f'p1{i}'].pos_hint == {"center_x": self.sw_f_se[0], "center_y": self.sw_f_se[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.ne_f_se[0], "center_y": self.ne_f_se[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.sw_f_se[0], "center_y": self.sw_f_se[1]}) and self.ids[f'p1{i}'].icon == "record-circle" and self.ids[f'p1{i}'].text_color == [0,0.2,0.21,0.31]:
                    self.ids[f'p1{i}'].text_color = 245/255, 5/255, 237/255
            for i in range(1, 21):
                if (self.ids[f'p1{i}'].pos_hint == {"center_x": self.w_f_se[0], "center_y": self.w_f_se[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.sw_f_se[0], "center_y": self.sw_f_se[1]}) and self.ids[f'p1{i}'].icon != "record-circle":
                    if self.ids.common10.pos_hint == {"center_x": self.xw_f_se[0], "center_y": self.xw_f_se[1]} or self.ids.common10.pos_hint == {"center_x": self.xsw_f_se[0], "center_y": self.xsw_f_se[1]}:
                        mid = ((self.ids.common10.pos_hint['center_x'] + pb_co[0])/2 , (self.ids.common10.pos_hint['center_y'] + pb_co[1])/2)
                        for j in range(1, 21):
                            if (self.ids[f'p2{j}'].pos_hint == {"center_x": self.w_f_se[0], "center_y": self.w_f_se[1]} or self.ids[f'p2{j}'].pos_hint == {"center_x": self.sw_f_se[0], "center_y": self.sw_f_se[1]}) and self.ids[f'p2{j}'].icon == "account":
                                if self.ids[f'p2{j}'].pos_hint == {'center_x': mid[0], 'center_y': mid[1]}:
                                    self.ids.common10.text_color = 0,0.2,0.21,0.31  
                        for j in range(1, 21):
                            if (self.ids[f'p1{j}'].pos_hint == {"center_x": self.w_f_se[0], "center_y": self.w_f_se[1]} or self.ids[f'p1{j}'].pos_hint == {"center_x": self.sw_f_se[0], "center_y": self.sw_f_se[1]}) and self.ids[f'p1{j}'].icon == "account":
                                if self.ids[f'p1{j}'].pos_hint == {'center_x': mid[0], 'center_y': mid[1]}:
                                    self.ids.common10.text_color = 245/255, 5/255, 237/255 
                    for i in range(1, 21):
                        if (self.ids[f'p2{i}'].pos_hint == {"center_x": self.xw_f_se[0], "center_y": self.xw_f_se[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.xsw_f_se[0], "center_y": self.xsw_f_se[1]}) and self.ids[f'p2{i}'].text_color == [0,0.2,0.21,0.31] and self.ids[f'p2{i}'].icon == "record-circle":
                            midp1 = ((self.ids[f'p2{i}'].pos_hint['center_x'] + pb_co[0])/2, (self.ids[f'p2{i}'].pos_hint['center_y'] + pb_co[1])/2)
                            for j in range(1, 21):
                                if (self.ids[f'p2{j}'].pos_hint == {"center_x": self.w_f_se[0], "center_y": self.w_f_se[1]} or self.ids[f'p2{j}'].pos_hint == {"center_x": self.sw_f_se[0], "center_y": self.sw_f_se[1]}) and self.ids[f'p2{j}'].icon == "account":
                                    if self.ids[f'p2{j}'].pos_hint == {'center_x': midp1[0], 'center_y': midp1[1]}:
                                        self.ids[f'p2{i}'].text_color = 0,0.2,0.21,0.31   
                        if (self.ids[f'p1{i}'].pos_hint == {"center_x": self.xw_f_se[0], "center_y": self.xw_f_se[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.xsw_f_se[0], "center_y": self.xsw_f_se[1]}) and self.ids[f'p1{i}'].text_color == [0,0.2,0.21,0.31] and self.ids[f'p1{i}'].icon == "record-circle":
                            midp11 = ((self.ids[f'p1{i}'].pos_hint['center_x'] + pb_co[0])/2, (self.ids[f'p1{i}'].pos_hint['center_y'] + pb_co[1])/2)
                            for j in range(1, 21):
                                if (self.ids[f'p2{j}'].pos_hint == {"center_x": self.w_f_se[0], "center_y": self.w_f_se[1]} or self.ids[f'p2{j}'].pos_hint == {"center_x": self.sw_f_se[0], "center_y": self.sw_f_se[1]}) and self.ids[f'p2{j}'].icon == "account":
                                    if self.ids[f'p2{j}'].pos_hint == {'center_x': midp11[0], 'center_y': midp11[1]}:
                                        self.ids[f'p1{i}'].text_color = 0,0.2,0.21,0.31   
                    for i in range(1, 21):
                        if (self.ids[f'p2{i}'].pos_hint == {"center_x": self.xw_f_se[0], "center_y": self.xw_f_se[1]} or self.ids[f'p2{i}'].pos_hint == {"center_x": self.xsw_f_se[0], "center_y": self.xsw_f_se[1]}) and self.ids[f'p2{i}'].text_color == [0,0.2,0.21,0.31] and self.ids[f'p2{i}'].icon == "record-circle":
                            midp1 = ((self.ids[f'p2{i}'].pos_hint['center_x'] + pb_co[0])/2, (self.ids[f'p2{i}'].pos_hint['center_y'] + pb_co[1])/2)
                            for j in range(1, 21):
                                if (self.ids[f'p1{j}'].pos_hint == {"center_x": self.w_f_se[0], "center_y": self.w_f_se[1]} or self.ids[f'p1{j}'].pos_hint == {"center_x": self.sw_f_se[0], "center_y": self.sw_f_se[1]}) and self.ids[f'p1{j}'].icon == "account":
                                    if self.ids[f'p1{j}'].pos_hint == {'center_x': midp1[0], 'center_y': midp1[1]}:
                                        self.ids[f'p2{i}'].text_color = 245/255, 5/255, 237/255
                        if (self.ids[f'p1{i}'].pos_hint == {"center_x": self.xw_f_se[0], "center_y": self.xw_f_se[1]} or self.ids[f'p1{i}'].pos_hint == {"center_x": self.xsw_f_se[0], "center_y": self.xsw_f_se[1]}) and self.ids[f'p1{i}'].text_color == [0,0.2,0.21,0.31] and self.ids[f'p1{i}'].icon == "record-circle":
                            midp11 = ((self.ids[f'p1{i}'].pos_hint['center_x'] + pb_co[0])/2, (self.ids[f'p1{i}'].pos_hint['center_y'] + pb_co[1])/2)
                            for j in range(1, 21):
                                if (self.ids[f'p1{j}'].pos_hint == {"center_x": self.w_f_se[0], "center_y": self.w_f_se[1]} or self.ids[f'p1{j}'].pos_hint == {"center_x": self.sw_f_se[0], "center_y": self.sw_f_se[1]}) and self.ids[f'p1{j}'].icon == "account":
                                    if self.ids[f'p1{j}'].pos_hint == {'center_x': midp11[0], 'center_y': midp11[1]}:
                                        self.ids[f'p1{i}'].text_color = 245/255, 5/255, 237/255  
                
                
    def shift(self, cme):
        myfirst = self.p1
        points = myfirst.pos_hint 
        mypoint = cme.pos_hint
        for i in range(1,21):
            if self.ids[f'p1{i}'].pos_hint == points:
                for i in range(1, 21):
                    if self.ids[f'p2{i}'].icon == "account": 
                        self.ids[f'p2{i}'].disabled = False
                    if self.ids[f'p1{i}'].icon == "account": 
                        self.ids[f'p1{i}'].disabled = True
                        self.ids[f'p1{i}'].disabled_color = self.player1_color
        self.button_clicked.stop()
        for i in range(1,21):
            if self.ids[f'p2{i}'].pos_hint == points:
                for i in range(1, 21):
                    if self.ids[f'p1{i}'].icon == "account": 
                        self.ids[f'p1{i}'].disabled = False
                    if self.ids[f'p2{i}'].icon == "account": 
                        self.ids[f'p2{i}'].disabled = True
                        self.ids[f'p2{i}'].disabled_color = self.player2_color
        midp2c = ((mypoint['center_x'] + points['center_x'])/2, (mypoint['center_y'] + points['center_y'])/2)
        for i in range(1, 21):
            if self.ids[f'p1{i}'].pos_hint == {"center_x": midp2c[0], "center_y": midp2c[1]}:
                self.ids[f'p1{i}'].text_color = 0,0.2,0.21,0.31  
                self.ids[f'p1{i}'].icon = "record-circle"
                self.shift_sound.play()
                self.m = self.m + 1
                for i in range(1, self.m + 1):
                    self.ids[f'po2{i}'].color = self.player1_color
                if self.m == 20:
                    self.shift_sound.stop()
                    self.winning_sound.play()
                    self.game_finish_alert("Player2", self.player2_color)
        for i in range(1, 21):
            if self.ids[f'p2{i}'].pos_hint == {"center_x": midp2c[0], "center_y": midp2c[1]}:
                self.ids[f'p2{i}'].text_color = 0,0.2,0.21,0.31  
                self.ids[f'p2{i}'].icon = "record-circle"
                self.shift_sound.play()
                self.n = self.n + 1
                for i in range(1, self.n + 1):
                    self.ids[f'po1{i}'].color = self.player2_color
                if self.n == 20:
                    self.shift_sound.stop()
                    self.winning_sound.play()
                    self.game_finish_alert("Player1", self.player1_color)
        myfirst.pos_hint = mypoint
        cme.pos_hint =  points
        self.ids[f'common10'].text_color =  0,0.2,0.21,0.31
        for i in range(1, 21):
            if self.ids[f'p1{i}'].icon == "record-circle" or self.ids[f'p1{i}'].text_color == [245/255, 5/255, 237/255]:
                self.ids[f'p1{i}'].text_color = 0,0.2,0.21,0.31
        for i in range(1, 21):
            if self.ids[f'p2{i}'].icon == "record-circle" or self.ids[f'p2{i}'].text_color == [245/255, 5/255, 237/255]:
                self.ids[f'p2{i}'].text_color = 0,0.2,0.21,0.31

    def restore(self):
        self.ids.p11.pos_hint= {"center_x": 0, "center_y": 1}
        self.ids.p12.pos_hint= {"center_x": 0.25, "center_y": 1}
        self.ids.p13.pos_hint= {"center_x": 0.5, "center_y": 1}
        self.ids.p14.pos_hint= {"center_x": 0.75, "center_y": 1}
        self.ids.p15.pos_hint= {"center_x": 1, "center_y": 1}
        self.ids.p16.pos_hint= {"center_x":0.25,"center_y":7/8}
        self.ids.p17.pos_hint= {"center_x":.5,"center_y":7/8}
        self.ids.p18.pos_hint= {"center_x":0.75,"center_y":7/8}
        self.ids.p19.pos_hint= {"center_x":0,"center_y":3/4}
        self.ids.p110.pos_hint= {"center_x":.25,"center_y":3/4}
        self.ids.p111.pos_hint= {"center_x":0.5,"center_y":3/4}
        self.ids.p112.pos_hint= {"center_x":.75,"center_y":3/4}
        self.ids.p113.pos_hint= {"center_x":1,"center_y":3/4}
        self.ids.p114.pos_hint= {"center_x":0,"center_y":5/8}
        self.ids.p115.pos_hint= {"center_x":0.25,"center_y":5/8}
        self.ids.p116.pos_hint= {"center_x":.5,"center_y":5/8}
        self.ids.p117.pos_hint= {"center_x":0.75,"center_y":5/8}
        self.ids.p118.pos_hint= {"center_x":1,"center_y":5/8}
        self.ids.p119.pos_hint= {"center_x":0.75,"center_y":.5}
        self.ids.p120.pos_hint= {"center_x":1,"center_y":.5}

        self.ids.p21.pos_hint= {"center_x":0,"center_y":0}
        self.ids.p22.pos_hint= {"center_x":.25,"center_y":0}
        self.ids.p23.pos_hint= {"center_x":0.5,"center_y":0}
        self.ids.p24.pos_hint= {"center_x":.75,"center_y":0}
        self.ids.p25.pos_hint= {"center_x":1,"center_y":0}
        self.ids.p26.pos_hint= {"center_x":0.25,"center_y":1/8}
        self.ids.p27.pos_hint=  {"center_x":.5,"center_y":1/8}
        self.ids.p28.pos_hint= {"center_x":0.75,"center_y":1/8}
        self.ids.p29.pos_hint= {"center_x":0,"center_y":1/4}
        self.ids.p210.pos_hint={"center_x":.25,"center_y":1/4}
        self.ids.p211.pos_hint= {"center_x":0.5,"center_y":1/4}
        self.ids.p212.pos_hint= {"center_x":.75,"center_y":1/4}
        self.ids.p213.pos_hint= {"center_x":1,"center_y":1/4}
        self.ids.p214.pos_hint={"center_x":0,"center_y":3/8}
        self.ids.p215.pos_hint= {"center_x":0.25,"center_y":3/8}
        self.ids.p216.pos_hint= {"center_x":.5,"center_y":3/8}
        self.ids.p217.pos_hint= {"center_x":0.75,"center_y":3/8}
        self.ids.p218.pos_hint= {"center_x":1,"center_y":3/8}
        self.ids.p219.pos_hint= {"center_x":0,"center_y":.5}
        self.ids.p220.pos_hint= {"center_x":0.25,"center_y":.5}
        self.ids.common10.pos_hint= {'center_x': 0.5,'center_y': 0.5}
        self.ids.common10.text_color = 0,0.2,0.21,0.31
        for i in range(1, 21):
            self.ids[f'p1{i}'].text_color = self.player1_color
            self.ids[f'p1{i}'].icon = "account"
            self.ids[f'p1{i}'].disabled = False
            self.ids[f'p2{i}'].text_color = self.player2_color
            self.ids[f'p2{i}'].icon = "account"
            self.ids[f'p2{i}'].disabled = False
        self.m = 0
        self.n = 0
        for i in range(1, 21):
            self.ids[f'po1{i}'].color = self.ids.p1.md_bg_color
            self.ids[f'po2{i}'].color = self.ids.p2.md_bg_color


        
    def game_finish_alert(self,player, pcolor):
        if not self.dialog:
            self.dialog = MDDialog(
                auto_dismiss = False,
                type = "custom",
                content_cls = GameFinishMessage(textp=f'{player} Win', color=pcolor),
                size_hint=(0.85, 0.3),
                buttons=[
                MDFillRoundFlatIconButton(icon = "play", text='Play again',on_release=self.dialog_close), 
                MDFillRoundFlatIconButton(icon="exit-to-app", text="Exit!", on_release = self.exit) 
                ]
            )
        self.dialog.open()
    def dialog_close(self, *args):
        self.winning_sound.stop()
        self.dialog.dismiss(force=True)
        self.restore()
    def exit(self, *args):
        self.winning_sound.stop()
        MDApp.get_running_app().stop()
