import Master
import Gameplay


master = Master.Master();
gameplay = Gameplay.Gameplay();

master.setGameplay(gameplay);

master.onStart();