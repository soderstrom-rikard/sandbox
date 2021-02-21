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

namespace GStest2
{
    public partial class Namn : Form
    {
        public Namn()
        {
            InitializeComponent();
        }

        private void CreateTestB_Click(object sender, EventArgs e)
        {
            //WaterflowTB.Text;
            //TimeTB.Text;
            //PulsintervalTB.Text;

           // DataGridViewRow NewTest = new DataGridViewRow();
           // object[] NewTestData = new object[]
           // {
           // WaterflowTB.Text, TimeTB.Text, PulsintervalTB.Text
           // };
           // NewTest.SetValues(NewTestData);

            int rowindex = TestTable1.Rows.Add();
            var row = TestTable1.Rows[rowindex];

            row.Cells["WaterflowT"].Value = WaterflowTB.Text;
            row.Cells["TimeT"].Value = TimeTB.Text;
            row.Cells["PulsintervalT"].Value = PulsintervalTB.Text;

        }

        private void button1_Click(object sender, EventArgs e)
        {
            saveFileDialog1.AddExtension = true;
            saveFileDialog1.Filter = "comma-separated values file (*.csv)|*.csv";
            var TEMP = saveFileDialog1.ShowDialog();
            if (TEMP == DialogResult.OK)
            {
                String csvdata = "";

                foreach (DataGridViewRow row in TestTable1.Rows)
                {
                    foreach (DataGridViewCell column in row.Cells)
                    {
                        csvdata += column.Value + ",";
                    }
                    csvdata += "\n";
                }
                File.WriteAllText(saveFileDialog1.FileName, csvdata);
               
                        }
        }

        private void saveFileDialog1_FileOk(object sender, CancelEventArgs e)
        {

        }
    }
}