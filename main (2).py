class player:
  def play(self):
    print("the player is playing cricket.")
class batsman(player):
  def play(self):
    print("batsman is batting")
class bowler(player):
  def play(self):
    print("the bowler is bowling")
if __name__=="__main__":
  Batsman=batsman()
  Bowler=bowler()
  Batsman.play()
  Bowler.play()
  

      
        
  