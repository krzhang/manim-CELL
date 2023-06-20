from manim import *

class Induction(Scene):

  boards = [[-2, 0, 0], [0, 2, 0], [2, 0, 0]]
  bps = [[-3, 0, 0], [0, 3, 0], [3, 0, 0]]

  def construct(self):

    wb1 = Rectangle(width=0.3, height=4.0, fill_color=WHITE, fill_opacity=0.8).shift(bps[0])
    wb2 = Rectangle(width=4.0, height=0.3, fill_color=WHITE, fill_opacity=0.8).shift(bps[1])
    wb3 = Rectangle(width=0.3, height=4.0, fill_color=WHITE, fill_opacity=0.8).shift(bps[2])
    wbs = Group(wb1, wb2, wb3)
    
    b1 = Brace(wb1, direction=[0, -1, 0])
    b1text = b1.get_text("Whiteboard 1")
    b2 = Brace(wb2, direction=[0, 1, 0])
    b2text = b2.get_text("Whiteboard 2")
    b3 = Brace(wb3, direction=[0, -1, 0])
    b3text = b3.get_text("Whiteboard 3")
    b1text.shift([0, 0.3, 0])
    b2text.shift([0, -0.3, 0])
    b3text.shift([0, 0.3, 0])
    ApplyMethod(b1text.scale, 0.5)
    ApplyMethod(b2text.scale, 0.5)
    ApplyMethod(b3text.scale, 0.5)

    self.add(b1text, b2text, b3text)
    
    circ1 = Circle(radius=0.3, color=GREEN_A).shift([-2-0.4, -0.4, 0])
    circ2 = Circle(radius=0.3, color=GREEN_A).shift([-2+0.4, -0.4, 0])
    circ3 = Circle(radius=0.3, color=GREEN_A).shift([-2-0.4, +0.4, 0])
    circ4 = Circle(radius=0.3, color=GREEN_A).shift([-2+0.4, +0.4, 0])
    circle = Group(circ1, circ2, circ3, circ4)

    circ21 = Circle(radius=0.3, color=BLUE_A).shift([-0.3, 2-0.33, 0])
    circ22 = Circle(radius=0.3, color=BLUE_A).shift([+0.38, 2+0.0, 0])
    circ23 = Circle(radius=0.3, color=BLUE_A).shift([-0.3, 2+0.33, 0])
    star = Group(circ21, circ22, circ23)

    circ31 = Circle(radius=0.3, color=RED_A).shift([2-0.4, -0.4, 0])
    circ32 = Circle(radius=0.3, color=RED_A).shift([2+0.4, -0.4, 0])
    circ33 = Circle(radius=0.3, color=RED_A).shift([2-0.4, +0.4, 0])
    circ34 = Circle(radius=0.3, color=RED_A).shift([2+0.4, +0.4, 0])
    square = Group(circ31, circ32, circ33, circ34)
   

    mobjects = [circle, star, square]
    
    locations = boards.copy()
    self.add(wbs)
    self.add(circle)
    self.add(star)
    self.add(square)
    
    self.wait(2)

    args = []
    locations = locations[1:] + locations[:1]    
    for loc, mob in zip(locations, mobjects):
      mob.generate_target()
      mob.target.move_to(loc)
      args.append(MoveToTarget(mob))

    self.play(*args)

    self.wait(2)

    args = []
    locations = locations[1:] + locations[:1]    
    for loc, mob in zip(locations, mobjects):
      mob.generate_target()
      mob.target.move_to(loc)
      args.append(MoveToTarget(mob))

    self.play(*args)

    self.wait(2)

    args = []
    locations = locations[1:] + locations[:1]    
    for loc, mob in zip(locations, mobjects):
      mob.generate_target()
      mob.target.move_to(loc)
      args.append(MoveToTarget(mob))

    self.play(*args)

    self.wait(2)

class Robot(object):
  def __init__(self, box, pos):
    self.box = box
    self.text = Text("112").move_to(pos)
    self.pos = pos
    
  def move_args(self, inc):
    """
    inc: -1 = left, 1 = right
    """
    args = []
    new_loc = self.pos.copy()
    new_loc[0] += inc*1.5
    
    self.box.generate_target()
    self.box.target.move_to(new_loc)
    args.append(MoveToTarget(self.box))
    if self.text:
      self.text.generate_target()
      self.text.target.move_to(new_loc)
      args.append(MoveToTarget(self.text))
    self.pos = new_loc
    return args

class Recursion(Scene):
  pos_text = ["1", "2", "3", "4", "5", "6", "7"]
  ID_text = ["101", "112", "123", "134", "145", "156", "167", "178"]
  
  def construct(self):
    IDs = {}
    for x in range(-3, 4):
      text = Text(pos_text[x+3]).move_to([x*1.5,1,0])
      self.add(text)
      IDs[ID_text[x+3]] = Text(ID_text[x+3]).move_to([x*1.5,0,0])
      self.add(IDs[ID_text[x+3]])
    pos = [-3*1.5, -1, 0]
    box = Rectangle(width=1, height=1, color=BLUE_A).shift(pos)
    rob = Robot(box, pos)
    self.add(box)
    self.add(rob.text)

    bottom_text = Text("pick up 101").move_to([0, 2, 0])
    self.add(bottom_text)
    self.wait(2)
    self.remove(bottom_text)    
    self.play(IDs["101"].animate.move_to([-3*1.5, -0.5, 0]))
  
    bottom_text = Text("compare with 101").move_to([0, 2, 0])
    self.add(bottom_text)
    self.wait(2)
    self.remove(bottom_text)    
    self.play(IDs["101"].animate.set_color(YELLOW_A), rob.text.animate.set_color(YELLOW_A))

    bottom_text = Text("put back 101").move_to([0, 2, 0])
    self.add(bottom_text)
    self.wait(2)
    self.remove(bottom_text)    
    self.play(IDs["101"].animate.set_color(WHITE), rob.text.animate.set_color(WHITE))
    self.play(IDs["101"].animate.move_to([-3*1.5, 0, 0]))
    
    bottom_text = Text("move right by R=3").move_to([0, 2, 0])
    self.add(bottom_text)
    self.wait(2)
    self.remove(bottom_text)
    self.play(*rob.move_args(1))
    self.play(*rob.move_args(1))
    self.play(*rob.move_args(1))

    bottom_text = Text("pick up 134").move_to([0, 2, 0])
    self.add(bottom_text)
    self.wait(2)
    self.remove(bottom_text)    
    self.play(IDs["134"].animate.move_to([0, -0.5, 0]))
  
    bottom_text = Text("compare with 134").move_to([0, 2, 0])
    self.add(bottom_text)
    self.wait(2)
    self.remove(bottom_text)    
    self.play(IDs["134"].animate.set_color(YELLOW_A), rob.text.animate.set_color(YELLOW_A))

    bottom_text = Text("put back 134").move_to([0, 2, 0])
    self.add(bottom_text)
    self.wait(2)
    self.remove(bottom_text)    
    self.play(IDs["134"].animate.set_color(WHITE), rob.text.animate.set_color(WHITE))
    self.play(IDs["134"].animate.move_to([0, 0, 0]))
    
    bottom_text = Text("move left by L=2").move_to([0, 2, 0])
    self.add(bottom_text)
    self.wait(2)
    self.remove(bottom_text)    
    self.play(*rob.move_args(-1))
    self.play(*rob.move_args(-1))

    bottom_text = Text("pick up 112").move_to([0, 2, 0])
    self.add(bottom_text)
    self.wait(2)
    self.remove(bottom_text)    
    self.play(IDs["112"].animate.move_to([-2*1.5, -0.5, 0]))

    bottom_text = Text("compare with 112").move_to([0, 2, 0])
    self.add(bottom_text)
    self.wait(2)
    self.remove(bottom_text)    
    self.play(IDs["112"].animate.set_color(YELLOW_A), rob.text.animate.set_color(YELLOW_A))

    bottom_text = Text("stop and light on (success!!)").move_to([0, 2, 0])
    self.add(bottom_text)
    self.wait(2)
    self.remove(bottom_text)    
    self.play(IDs["112"].animate.set_color(GREEN_B), rob.text.animate.set_color(GREEN_B))
    self.wait(2)
