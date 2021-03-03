using System;
using System.Threading;

namespace Vattenrening
{
  public enum ProgramSteps { Off, Initialize, StartCirculation, WaitForAirPulse, WaitForPulseLength, CloseAirValve, StopCirculation };

  public class WCProgram
  {
    /*Automatiska "Setters" och "Getters" - behöver inte skriva ut hela funktionen exempel:
    
    Om man gör allt manuellt
    public string GetSomeString() { return myPrivateString; }
    public void SetSomeString(string newString) { myPrivateString = newString }
    private string myPrivateString;
    
    Automatisk funktion
    public string Something {get; set;}
     */
    
    public ProgramSteps CurrentStep { set; get; }
    public string Name { get; set; }
    public int WaterFlow { get; set; }
    public int PulseInterval { get; set; }
    public int PulseLength { get; set; }
    public string Desc { get; set; }

    public DateTime LastPulse { set; get; }

  }

  public enum MotorStatus { Off, On, Error };

  public enum ValveStatus { Closed, Open, Error };

  public interface IWaterCleaningAdapter

  {
    void Initialize(SynchronizationContext syncContext);

    //Default värde om inget annat sägs, se rad 108 (Start intervallet )
    void Start(int interval = 1000);


    void Stop();

    void StartCirculationPump(int effect);

    void StopCirculationPump();

    MotorStatus GetCirculationPumpStatus();

    void OpenAirValve();

    void CloseAirValve();

    ValveStatus GetAirValveStatus();
  }

  public class WaterCleaningSimulator : IWaterCleaningAdapter
  {
    readonly System.Timers.Timer timer_refresh_gui = new System.Timers.Timer();

    public Action EquipmentChangedEvent;

    public void CloseAirValve()
    {
      if (valveStatus == ValveStatus.Open)
      {
        //Anropa PLC-funktion för att stänga ventilen
        valveStatus = ValveStatus.Closed;
      }
      else if (valveStatus == ValveStatus.Error)
      {
        //Skickar felmeddelande
        throw new InvalidOperationException("ValFusk");
      }
      else if (valveStatus == ValveStatus.Closed)
      {
        //Redan stängd - utvärdera om det är tillåtet tillstånd
      }
    }

    public ValveStatus GetAirValveStatus()
    {
      return valveStatus;
    }

    public MotorStatus GetCirculationPumpStatus()
    {
      return motorStatus;
    }

    //Vet inte vad det innebär
    private SynchronizationContext _syncContext = null;

    public void Initialize(SynchronizationContext syncContext)
    {
      _syncContext = syncContext;

      valveStatus = ValveStatus.Closed;
      motorStatus = MotorStatus.Off;

      timer_refresh_gui.Elapsed += Timer_Refresh_GUI_Handler;
    }

    // Hur ofta det uppdaterar informationen, sätter nya defaultvärdet för hur frekvent det uppdateras.
    public void Start(int interval = 100)
    {
      timer_refresh_gui.Interval = interval;
      timer_refresh_gui.Start();
    }
    public void Stop()
    {
      timer_refresh_gui.Stop();
    }

    //När timern räknat klart kommer det uppdatera status för motor och ventil
    private void Timer_Refresh_GUI_Handler(object sender, System.Timers.ElapsedEventArgs e)
    {
      _syncContext.Post(o => EquipmentChangedEvent?.Invoke(), null);
    }

    public void OpenAirValve()
    {

      if (valveStatus == ValveStatus.Open)
      {
        //Redan öppen - utvärdera om det är tillåtet tillstånd
      }
      else if (valveStatus == ValveStatus.Error)
      {
        //Skickar felmeddelande
        throw new InvalidOperationException("ValFusk");
      }
      else if (valveStatus == ValveStatus.Closed)
      {
        //Anropa PLC-funktion för att öppna ventilen
        valveStatus = ValveStatus.Open;
      }
    }

    public void StartCirculationPump(int effect)
    {
      if (motorStatus == MotorStatus.On)
      {
        //Redan på - utvärdera om tillståndet är tillåtet
      }
      else if (motorStatus == MotorStatus.Error)
      {
        throw new InvalidOperationException("MotFusk");
      }
      else if (motorStatus == MotorStatus.Off)
      {
        //Anropa PLC-funktion för att starta motorn med viss effekt
        //Sätt in effekt
        motorStatus = MotorStatus.On;

      }
    }

    public void StopCirculationPump()
    {
      if (motorStatus == MotorStatus.On)
      {
        //Anropa PLC-funktion för att stanna motorn och stänga av effekt
        //Sätt in effekt
        motorStatus = MotorStatus.Off;
      }
      else if (motorStatus == MotorStatus.Error)
      {
        throw new InvalidOperationException("MotFusk");
      }
      else if (motorStatus == MotorStatus.Off)
      {
        //Redan på - utvärdera om tillståndet är tillåtet
      }
    }

    private MotorStatus motorStatus;
    private ValveStatus valveStatus;
  }
}
