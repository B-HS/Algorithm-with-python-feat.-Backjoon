while(1):
    a = float(input())
    if a < 0:
        break
    print("Objects weighing "+format(a, ".2f")+" on Earth will weigh " +
          format((a*0.167), ".2f")+" on the moon.")