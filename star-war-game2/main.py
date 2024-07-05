import random
import arcade
import time
import math
import threading

SCREEN_WIDTH =800
SCREEN_HIGHT =600


class starship(arcade.Sprite):
    def __init__(self):
        super().__init__(":resources:images/space_shooter/playerShip1_orange.png")
        self.center_x =SCREEN_WIDTH//2
        self.center_y =32
        self.width =40
        self.heigth=40
        self.angel=0
        self.speed =4
        self.change_angle =0
        self.bulet_list=[]
        self.bulet2_list=[]
        self.score =0
        self.live=3
        
        
        
    def fire(self):
        self.bulet_list.append(Bullet(self))    
        
    def xy_change(self):
        self.center_x += self.speed * self.change_x 
        self.center_y += self.speed * self.change_y
    
    def rotate(self):
        self.angle += self.speed * self.change_angle
    

class Enemy(arcade.Sprite):
    def __init__(self):
        super().__init__(":resources:images/space_shooter/playerShip1_green.png")
        self.center_x = random.randint(0,SCREEN_WIDTH)
        self.center_y = SCREEN_HIGHT+20
        self.change_y=0
        self.width =40
        self.heigth=40
        self.speed =4
        
        
    def move(self):
        
         self.center_y -=self.speed   
         
         
    def sound_H(self):
            arcade.play_sound(arcade.sound.Sound(':resources:sounds/hit3.wav'))    



class Bigenemy(arcade.Sprite):
    def __init__(self):
        super().__init__(":resources:images/space_shooter/playerShip1_green.png")
        self.center_x = SCREEN_WIDTH//2
        self.center_y = SCREEN_HIGHT-40
        self.change_y=0
        self.width =150
        self.heigth=150
        self.score =10
        self.bulet2_list=[]
       
    def fire2(self):
        self.bulet2_list.append(Bullet(self)) 
        
         
    
    def sound_H(self):
            arcade.play_sound(arcade.sound.Sound(':resources:sounds/hit3.wav'))
class Bullet(arcade.Sprite):
    def __init__(self,host):
        super().__init__(":resources:images/space_shooter/laserRed01.png")
        self.speed =6
        self.angle =host.angle
        self.center_x = host.center_x
        self.center_y =host.center_y
           
    def move(self):
        a=math.radians(self.angle)
        self.center_x +=-self.speed * math.sin(a)
        self.center_y +=self.speed * math.cos(a)
    def sound_B(self):
         arcade.play_sound(arcade.sound.Sound(':resources:sounds/laser1.wav'))  
          
    def move2(self):
         a=math.radians(self.angle)   
         self.center_y -=self.speed * math.cos(a)  

class Game(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH,SCREEN_HIGHT,"STAR WAR GAME 🚀")
        arcade.set_background_color(arcade.color.BLACK)
        self.background_image = arcade.load_texture(":resources:images/backgrounds/stars.png")
        self.me=starship()    
        self.big=Bigenemy()
        self.enemy_list =[]
        self.r=random.randint(5,8)
        self.start_time= time.time()
        self.my_thread=threading.Thread(target=self.add_enemy)
        self.my_thread.start()
    def on_draw(self): 
        
        arcade.start_render() 
        arcade.draw_lrwh_rectangle_textured(0,0,SCREEN_WIDTH,SCREEN_HIGHT,self.background_image)
        arcade.draw_text(f"Score: {self.me.score}",start_x= 670, start_y= 10 ,color=arcade.color.WHITE,font_size = 20)
        
        if self.me.live==3:
            arcade.draw_text(f" ❤   ❤   ❤ ",start_x= 10, start_y= 10 ,color=arcade.color.WHITE,font_size = 40)
        elif self.me.live==2:
        
            arcade.draw_text(f" ❤   ❤ ",start_x= 10, start_y= 10 ,color=arcade.color.WHITE,font_size = 40)
        elif self.me.live==1:
            arcade.draw_text(f" ❤ ",start_x= 10, start_y= 10 ,color=arcade.color.WHITE,font_size = 40)        
        elif self.me.live==0:
          self.background_image = arcade.load_texture("gameover.png") 
          arcade.draw_text(" GAME OVER ", start_x= 100, start_y= 250,color= arcade.color.WHITE, font_size =90)
          arcade.finish_render()
          time.sleep(3)
          exit()
         
        if self.me.score>10:  
         self.big.draw()
        self.me.draw()
        for enemy in self.enemy_list:
            enemy.draw()
           
        for bullet in self.me.bulet_list:
            bullet.draw()    
        
        for bullet in self.big.bulet2_list:
                bullet.draw()    
    def on_update(self,delta_time:float):
       
        self.end_time =time.time()
        self.me.rotate()
        self.me.xy_change()
       
    
       
          
        if self.me.score>10:    
         if (self.end_time)-(self.start_time)>2:    
                self.big.fire2()
                
            
        
    
        for enemy in self.enemy_list:
            
            enemy.move()
            if enemy.center_y<0:
                    self.enemy_list.remove(enemy) 
                    self.me.live-=1
                  
                   
        
        for bullet in self.me.bulet_list:
            bullet.move()
                
        
        for bullet in self.big.bulet2_list:
          
            bullet.move2()  
             
        for bullet in self.me.bulet_list:   
         for enemy in self.enemy_list:
              if arcade.check_for_collision(bullet, enemy):
                    enemy.sound_H()
                    self.me.bulet_list.remove(bullet)
                    self.enemy_list.remove(enemy)
                    self.me.score+=1
                    
        
         for bullet in self.me.bulet_list:
                if bullet.center_y>SCREEN_HIGHT:
                    self.me.bulet_list.remove(bullet)
                    
        
    def add_enemy(self):
        while True:
            self.enemy_list.append(Enemy()) 
            time.sleep(5)      
            for enemy in self.enemy_list:
                    enemy.speed += 1
                                         
                    
    def on_key_press(self, symbol: int, modifiers: int):
        if symbol==arcade.key.SPACE:
            self.me.fire()
     
            for bullet in self.me.bulet_list:
             bullet.sound_B() 
    
        
        
                    
        if symbol == arcade.key.F:
             self.me.change_angle = 1
        if symbol == arcade.key.J:
             self.me.change_angle = -1    
             
        if symbol == arcade.key.RIGHT:
                self.me.change_x = 1

        if symbol == arcade.key.LEFT:
            self.me.change_x = -1

        if symbol == arcade.key.UP:
            self.me.change_y = 1

        if symbol == arcade.key.DOWN:
            self.me.change_y = -1     
    def on_key_release(self, key, modifiers):
            if key == arcade.key.RIGHT or arcade.key.LEFT:
               self.me.change_angle = 0  
               self.me.change_y = 0
               self.me.change_x = 0
                  
                    
            

game=Game()            
arcade.run()
 