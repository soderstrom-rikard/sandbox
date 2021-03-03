using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using Vattenrening;
using System.Timers;
using System.Threading;

namespace GStest2
{


  public partial class Namn : Form
  {
    readonly WaterCleaningSimulator Vattensimulator = new WaterCleaningSimulator();

    readonly System.Timers.Timer timer = new System.Timers.Timer();

    public SynchronizationContext _syncContext = null;

    private WCProgram Program = new WCProgram();

    private void HandleTimer(Object source, ElapsedEventArgs e)
    {
      //En finare "if" funktion som styrs av "case", man jämför någonting till exempel en färg mot en specifik färg. En "State-maskin" - tänk kulhissprogrammering med våningar.
      var _t1 = (System.Timers.Timer) source;
      switch (Program.CurrentStep)
      {
        case ProgramSteps.Off:
          Program.CurrentStep = ProgramSteps.Initialize;
          break;

        case ProgramSteps.Initialize:
          Vattensimulator.Initialize(_syncContext);
          Vattensimulator.EquipmentChangedEvent += EquipmentChangedEvent;
          Vattensimulator.Start();
          Program.CurrentStep = ProgramSteps.StartCirculation;
          break;

        case ProgramSteps.StartCirculation:
          Vattensimulator.StartCirculationPump(Program.WaterFlow);
          Program.LastPulse = DateTime.UtcNow;
          Program.CurrentStep = ProgramSteps.WaitForAirPulse;
          break;

        case ProgramSteps.WaitForAirPulse:
          if (!_t1.Enabled) // stop button clicked
          {
           Program.CurrentStep = ProgramSteps.StopCirculation;
          }

          else if (DateTime.UtcNow > (Program.LastPulse + TimeSpan.FromSeconds(Program.PulseInterval)))
          {
            Vattensimulator.OpenAirValve();
            Program.CurrentStep = ProgramSteps.WaitForPulseLength;
          }

          break;

        case ProgramSteps.WaitForPulseLength:
          if (!_t1.Enabled) // stop button clicked
          {
           Program.CurrentStep = ProgramSteps.CloseAirValve;
          }
          else if (DateTime.UtcNow > (Program.LastPulse + TimeSpan.FromSeconds(Program.PulseInterval) + TimeSpan.FromSeconds(Program.PulseLength)))
          {
            Vattensimulator.CloseAirValve();
            Program.LastPulse = DateTime.UtcNow;
            Program.CurrentStep = ProgramSteps.WaitForAirPulse;
          }

          break;

        case ProgramSteps.CloseAirValve:
          Vattensimulator.CloseAirValve();
          Program.CurrentStep = ProgramSteps.StopCirculation;
          break;

        case ProgramSteps.StopCirculation:
          Vattensimulator.StopCirculationPump();
          Program.CurrentStep = ProgramSteps.Off;
          break;

        default:
          break;
      }
    }

    private void EquipmentChangedEvent()
    {
      UppdateMotorLB(Vattensimulator.GetCirculationPumpStatus());
      UppdateVentilLB(Vattensimulator.GetAirValveStatus());
    }

    private void UppdateMotorLB(MotorStatus motorStatus)
    {
      MotorLB.SetItemChecked(0, motorStatus == MotorStatus.On);
      MotorLB.SetItemChecked(1, motorStatus == MotorStatus.Off);
      MotorLB.SetItemChecked(2, motorStatus == MotorStatus.Error);
    }
    private void UppdateVentilLB(ValveStatus valveStatus)
    {
      VentilLB.SetItemChecked(0, valveStatus == ValveStatus.Open);
      VentilLB.SetItemChecked(1, valveStatus == ValveStatus.Closed);
      VentilLB.SetItemChecked(2, valveStatus == ValveStatus.Error);
    }

    public Namn()
    {
      InitializeComponent();

      timer.Elapsed += HandleTimer;

      _syncContext = SynchronizationContext.Current;
    }

    //Knapp för att skapa projekt
    private void CreateTestB_Click(object sender, EventArgs e)
    {
      int rowindex = TestTable1.Rows.Add();
      var row = TestTable1.Rows[rowindex];

      //Gör om sträng (Text) till objekt (Value) x5, vänster sida kopierar höger sida.
      row.Cells["ProjektnamnT"].Value = ProjektnamnTB.Text;
      row.Cells["WaterflowT"].Value = WaterflowTB.Text;
      row.Cells["TimeT"].Value = TimeTB.Text;
      row.Cells["PulsintervalT"].Value = PulsintervalTB.Text;
      row.Cells["BeskrivningT"].Value = BeskrivningTB.Text;

    }



    //Knapp för att spara
    private void SparaB_Click(object sender, EventArgs e)
    {
      saveFileDialog1.AddExtension = true;
      saveFileDialog1.Filter = "comma-separated values file (*.csv)|*.csv";
      var TEMP = saveFileDialog1.ShowDialog();

      if (TEMP == DialogResult.OK)
      {
        String csvdata = "";
        bool Firstrow = true;

        foreach (DataGridViewRow row in TestTable1.Rows)
        {
          //Ny rad
          if (Firstrow)
          {
            Firstrow = false;
          }
          else
          {
            csvdata += "\n";
          }

          bool FirstColumn = true;
          foreach (DataGridViewCell column in row.Cells)
          {
            //Skiljetecken
            if (FirstColumn)
            {
              csvdata += column.Value;
              FirstColumn = false;
            }
            else
            {
              csvdata += "," + column.Value;
            }
          }

        }
        File.WriteAllText(saveFileDialog1.FileName, csvdata);
      }
    }


    //Knapp för att ladda data från en fil
    private void LaddaB_Click(object sender, EventArgs e)
    {

      using (OpenFileDialog openFileDialog = new OpenFileDialog())
      {
        openFileDialog.InitialDirectory = @"C:\Users\scout\Desktop\UHT Praktik";
        openFileDialog.Filter = "txt files (*.txt)|*.txt|All files (*.*)|*.*";
        openFileDialog.FilterIndex = 2;
        openFileDialog.RestoreDirectory = true;

        if (openFileDialog.ShowDialog() == DialogResult.OK)
        {

          TestTable1.Rows.Clear();

          //Get the path of specified file
          var filePath = openFileDialog.FileName;

          //Read the contents of the file into a stream
          var fileStream = openFileDialog.OpenFile();



          using (StreamReader reader = new StreamReader(fileStream))
          {
            var fileContent = reader.ReadToEnd();
            string[] rows = fileContent.Split('\n');
            foreach (String rad in rows)
            {
              int rowindex = TestTable1.Rows.Add();
              var row = TestTable1.Rows[rowindex];
              int columnindex = 0;

              string[] columns = rad.Split(',');
              foreach (String column in columns)
              {

                row.Cells[columnindex].Value = column;
                //++ kort för öka värdet med 1
                columnindex++;
              }
            }

          }
        }
      }

      //MessageBox.Show(fileContent, "File Content at path: " + filePath, MessageBoxButtons.OK);
    }

    //Knapp för att köra test
    private void KorTestB_Click(object sender, EventArgs e)
    {
      if (TestTable1.SelectedRows.Count > 0)
      {
        DataGridViewRow row = TestTable1.SelectedRows[0];

        Program = new WCProgram()
        {
          CurrentStep = ProgramSteps.Off,
          Name = (string)row.Cells["ProjektnamnT"].Value,
          WaterFlow = int.Parse((string)row.Cells["WaterflowT"].Value),
          PulseInterval = int.Parse((string)row.Cells["TimeT"].Value),
          PulseLength = int.Parse((string)row.Cells["PulsintervalT"].Value),
          Desc = (string)row.Cells["BeskrivningT"].Value
        };
        ShowProgramInfo(Program);

        timer.Interval = 50; // 500 ms interval.
        timer.Start();
      }
    }

    private void ShowProgramInfo(WCProgram prog)
    {
      ProjektnamnTB.Text = prog.Name;
      WaterflowTB.Text = prog.WaterFlow.ToString();
      TimeTB.Text = prog.PulseLength.ToString();
      PulsintervalTB.Text = prog.PulseInterval.ToString();
      BeskrivningTB.Text = prog.Desc;
    }

    //Knapp för att rensa tabellen.
    private void RensaB_Click(object sender, EventArgs e)
    {
      TestTable1.Rows.Clear();
    }

    private void VentilLB_SelectedIndexChanged(object sender, EventArgs e)
    {

    }

    private void StoppaTestB_Click(object sender, EventArgs e)
    {
      //timer.Stop();
      Vattensimulator.Stop();
    }
  }
}
