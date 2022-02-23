def get_Days(days):
  if days == 1:
    return "(next day)"
  elif days>1:
    return f"({days} days later)"

  return ""


def add_time(start, duration,day=False):
  
  Week_days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
  
  new_time=""
  Days_Later=0
  Half=12
  Complete=24
  
  Time,AMPM=start.split(" ")
  Hours,Minutes=Time.split(":")
  
  PlusHours,PlusMinutes=duration.split(':')
  NewHour=0
  NewMinutes=0
  
  NewHour=int(Hours)+int(PlusHours)
  NewMinutes=int(Minutes)+int(PlusMinutes)

  if NewMinutes >= 60:
    NewHour += int(NewMinutes/60)
    NewMinutes = int(NewMinutes%60)

  if PlusHours or PlusMinutes: 
    if AMPM=='PM' and NewHour>Half:
      if NewHour%Complete >= 1:
        Days_Later +=1
      
    if NewHour>=Half:
      Days_Later += int(NewHour/Complete)

    tth= NewHour
    while True:
      
      if tth < Half:
        break
        
      if tth>=Half:
        if AMPM == 'AM':
          AMPM='PM'
        elif AMPM == 'PM':
          AMPM='AM'
        tth -=Half

  NewHour= int(NewHour%Half)
  NewMinutes= int(NewMinutes%60)
  if NewHour==0:
    NewHour=12
    
  new_time = f'{NewHour}:{NewMinutes:02} {AMPM}'

  if day:
    day = day.strip().lower()
    Select_day = int((Week_days.index(day)+Days_Later)%7)
    Current_day = Week_days[Select_day]
    new_time += f', {Current_day.title()} {get_Days(Days_Later)}'

  else:
    new_time = " ".join((new_time,get_Days(Days_Later)))

  return new_time.strip()