
namespace GStest2
{
    partial class Namn
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.TestTable1 = new System.Windows.Forms.DataGridView();
            this.WaterflowT = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.TimeT = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.PulsintervalT = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.CreateTestB = new System.Windows.Forms.Button();
            this.WaterflowTB = new System.Windows.Forms.TextBox();
            this.TimeTB = new System.Windows.Forms.TextBox();
            this.PulsintervalTB = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.fontDialog1 = new System.Windows.Forms.FontDialog();
            this.button1 = new System.Windows.Forms.Button();
            this.saveFileDialog1 = new System.Windows.Forms.SaveFileDialog();
            ((System.ComponentModel.ISupportInitialize)(this.TestTable1)).BeginInit();
            this.SuspendLayout();
            // 
            // TestTable1
            // 
            this.TestTable1.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.TestTable1.Columns.AddRange(new System.Windows.Forms.DataGridViewColumn[] {
            this.WaterflowT,
            this.TimeT,
            this.PulsintervalT});
            this.TestTable1.Location = new System.Drawing.Point(0, 0);
            this.TestTable1.Name = "TestTable1";
            this.TestTable1.Size = new System.Drawing.Size(343, 203);
            this.TestTable1.TabIndex = 0;
            // 
            // WaterflowT
            // 
            this.WaterflowT.HeaderText = "Vattenflöde";
            this.WaterflowT.Name = "WaterflowT";
            // 
            // TimeT
            // 
            this.TimeT.HeaderText = "Tid";
            this.TimeT.Name = "TimeT";
            // 
            // PulsintervalT
            // 
            this.PulsintervalT.HeaderText = "Pulsintervall";
            this.PulsintervalT.Name = "PulsintervalT";
            // 
            // CreateTestB
            // 
            this.CreateTestB.Location = new System.Drawing.Point(349, 180);
            this.CreateTestB.Name = "CreateTestB";
            this.CreateTestB.Size = new System.Drawing.Size(75, 23);
            this.CreateTestB.TabIndex = 1;
            this.CreateTestB.Text = "Skapa test";
            this.CreateTestB.UseVisualStyleBackColor = true;
            this.CreateTestB.Click += new System.EventHandler(this.CreateTestB_Click);
            // 
            // WaterflowTB
            // 
            this.WaterflowTB.Location = new System.Drawing.Point(349, 74);
            this.WaterflowTB.Name = "WaterflowTB";
            this.WaterflowTB.Size = new System.Drawing.Size(100, 20);
            this.WaterflowTB.TabIndex = 2;
            // 
            // TimeTB
            // 
            this.TimeTB.Location = new System.Drawing.Point(349, 113);
            this.TimeTB.Name = "TimeTB";
            this.TimeTB.Size = new System.Drawing.Size(100, 20);
            this.TimeTB.TabIndex = 3;
            // 
            // PulsintervalTB
            // 
            this.PulsintervalTB.Location = new System.Drawing.Point(349, 152);
            this.PulsintervalTB.Name = "PulsintervalTB";
            this.PulsintervalTB.Size = new System.Drawing.Size(100, 20);
            this.PulsintervalTB.TabIndex = 4;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(349, 58);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(61, 13);
            this.label1.TabIndex = 5;
            this.label1.Text = "Vattenflöde";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(349, 97);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(22, 13);
            this.label2.TabIndex = 6;
            this.label2.Text = "Tid";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(349, 136);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(63, 13);
            this.label3.TabIndex = 7;
            this.label3.Text = "Pulsintervall";
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(12, 209);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(75, 23);
            this.button1.TabIndex = 8;
            this.button1.Text = "Save";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // saveFileDialog1
            // 
            this.saveFileDialog1.FileOk += new System.ComponentModel.CancelEventHandler(this.saveFileDialog1_FileOk);
            // 
            // Namn
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.button1);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.PulsintervalTB);
            this.Controls.Add(this.TimeTB);
            this.Controls.Add(this.WaterflowTB);
            this.Controls.Add(this.CreateTestB);
            this.Controls.Add(this.TestTable1);
            this.Name = "Namn";
            this.Text = "Form1";
            ((System.ComponentModel.ISupportInitialize)(this.TestTable1)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.DataGridView TestTable1;
        private System.Windows.Forms.Button CreateTestB;
        private System.Windows.Forms.TextBox WaterflowTB;
        private System.Windows.Forms.TextBox TimeTB;
        private System.Windows.Forms.TextBox PulsintervalTB;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.DataGridViewTextBoxColumn WaterflowT;
        private System.Windows.Forms.DataGridViewTextBoxColumn TimeT;
        private System.Windows.Forms.DataGridViewTextBoxColumn PulsintervalT;
        private System.Windows.Forms.FontDialog fontDialog1;
        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.SaveFileDialog saveFileDialog1;
    }
}

