
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
            this.ProjektnamnT = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.WaterflowT = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.TimeT = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.PulsintervalT = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.BeskrivningT = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.SkapaTestB = new System.Windows.Forms.Button();
            this.WaterflowTB = new System.Windows.Forms.TextBox();
            this.TimeTB = new System.Windows.Forms.TextBox();
            this.PulsintervalTB = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.fontDialog1 = new System.Windows.Forms.FontDialog();
            this.SparaB = new System.Windows.Forms.Button();
            this.saveFileDialog1 = new System.Windows.Forms.SaveFileDialog();
            this.ProjektnamnTB = new System.Windows.Forms.TextBox();
            this.label5 = new System.Windows.Forms.Label();
            this.Beskrivning = new System.Windows.Forms.Label();
            this.BeskrivningTB = new System.Windows.Forms.RichTextBox();
            this.StopTestB = new System.Windows.Forms.Button();
            this.LaddaB = new System.Windows.Forms.Button();
            this.openFileDialog1 = new System.Windows.Forms.OpenFileDialog();
            this.KorTestB = new System.Windows.Forms.Button();
            this.RensaB = new System.Windows.Forms.Button();
            this.MotorLB = new System.Windows.Forms.CheckedListBox();
            this.VentilLB = new System.Windows.Forms.CheckedListBox();
            this.label4 = new System.Windows.Forms.Label();
            this.label7 = new System.Windows.Forms.Label();
            ((System.ComponentModel.ISupportInitialize)(this.TestTable1)).BeginInit();
            this.SuspendLayout();
            // 
            // TestTable1
            // 
            this.TestTable1.AllowUserToAddRows = false;
            this.TestTable1.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.TestTable1.Columns.AddRange(new System.Windows.Forms.DataGridViewColumn[] {
                    this.ProjektnamnT,
                    this.WaterflowT,
                    this.TimeT,
                    this.PulsintervalT,
                    this.BeskrivningT});
            this.TestTable1.Location = new System.Drawing.Point(12, 12);
            this.TestTable1.MultiSelect = false;
            this.TestTable1.Name = "TestTable1";
            this.TestTable1.SelectionMode = System.Windows.Forms.DataGridViewSelectionMode.FullRowSelect;
            this.TestTable1.Size = new System.Drawing.Size(542, 203);
            this.TestTable1.TabIndex = 0;
            // 
            // ProjektnamnT
            // 
            this.ProjektnamnT.HeaderText = "Projektnamn";
            this.ProjektnamnT.Name = "ProjektnamnT";
            // 
            // WaterflowT
            // 
            this.WaterflowT.HeaderText = "Vattenflöde";
            this.WaterflowT.Name = "WaterflowT";
            // 
            // TimeT
            // 
            this.TimeT.HeaderText = "Tid (s)";
            this.TimeT.Name = "TimeT";
            // 
            // PulsintervalT
            // 
            this.PulsintervalT.HeaderText = "Pulsintervall";
            this.PulsintervalT.Name = "PulsintervalT";
            // 
            // BeskrivningT
            // 
            this.BeskrivningT.HeaderText = "Beskrivning";
            this.BeskrivningT.Name = "BeskrivningT";
            // 
            // SkapaTestB
            // 
            this.SkapaTestB.Location = new System.Drawing.Point(282, 354);
            this.SkapaTestB.Name = "SkapaTestB";
            this.SkapaTestB.Size = new System.Drawing.Size(75, 23);
            this.SkapaTestB.TabIndex = 1;
            this.SkapaTestB.Text = "Skapa test";
            this.SkapaTestB.UseVisualStyleBackColor = true;
            this.SkapaTestB.Click += new System.EventHandler(this.CreateTestB_Click);
            // 
            // WaterflowTB
            // 
            this.WaterflowTB.Location = new System.Drawing.Point(282, 248);
            this.WaterflowTB.Name = "WaterflowTB";
            this.WaterflowTB.Size = new System.Drawing.Size(100, 20);
            this.WaterflowTB.TabIndex = 2;
            // 
            // TimeTB
            // 
            this.TimeTB.Location = new System.Drawing.Point(282, 287);
            this.TimeTB.Name = "TimeTB";
            this.TimeTB.Size = new System.Drawing.Size(100, 20);
            this.TimeTB.TabIndex = 3;
            // 
            // PulsintervalTB
            // 
            this.PulsintervalTB.Location = new System.Drawing.Point(282, 326);
            this.PulsintervalTB.Name = "PulsintervalTB";
            this.PulsintervalTB.Size = new System.Drawing.Size(100, 20);
            this.PulsintervalTB.TabIndex = 4;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(282, 232);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(61, 13);
            this.label1.TabIndex = 5;
            this.label1.Text = "Vattenflöde";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(282, 271);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(22, 13);
            this.label2.TabIndex = 6;
            this.label2.Text = "Tid";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(282, 310);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(63, 13);
            this.label3.TabIndex = 7;
            this.label3.Text = "Pulsintervall";
            // 
            // SparaB
            // 
            this.SparaB.Location = new System.Drawing.Point(366, 354);
            this.SparaB.Name = "SparaB";
            this.SparaB.Size = new System.Drawing.Size(75, 23);
            this.SparaB.TabIndex = 8;
            this.SparaB.Text = "Spara";
            this.SparaB.UseVisualStyleBackColor = true;
            this.SparaB.Click += new System.EventHandler(this.SparaB_Click);
            // 
            // ProjektnamnTB
            // 
            this.ProjektnamnTB.Location = new System.Drawing.Point(12, 248);
            this.ProjektnamnTB.Name = "ProjektnamnTB";
            this.ProjektnamnTB.Size = new System.Drawing.Size(100, 20);
            this.ProjektnamnTB.TabIndex = 9;
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Location = new System.Drawing.Point(9, 232);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(66, 13);
            this.label5.TabIndex = 12;
            this.label5.Text = "Projektnamn";
            // 
            // Beskrivning
            // 
            this.Beskrivning.AutoSize = true;
            this.Beskrivning.Location = new System.Drawing.Point(9, 271);
            this.Beskrivning.Name = "Beskrivning";
            this.Beskrivning.Size = new System.Drawing.Size(62, 13);
            this.Beskrivning.TabIndex = 13;
            this.Beskrivning.Text = "Beskrivning";
            // 
            // BeskrivningTB
            // 
            this.BeskrivningTB.Location = new System.Drawing.Point(12, 287);
            this.BeskrivningTB.Name = "BeskrivningTB";
            this.BeskrivningTB.Size = new System.Drawing.Size(249, 90);
            this.BeskrivningTB.TabIndex = 14;
            this.BeskrivningTB.Text = "";
            // 
            // StopTestB
            // 
            this.StopTestB.Location = new System.Drawing.Point(560, 383);
            this.StopTestB.Name = "StopTestB";
            this.StopTestB.Size = new System.Drawing.Size(75, 23);
            this.StopTestB.TabIndex = 16;
            this.StopTestB.Text = "Stoppa Test";
            this.StopTestB.UseVisualStyleBackColor = true;
            this.StopTestB.Click += new System.EventHandler(this.StoppaTestB_Click);
            // 
            // LaddaB
            // 
            this.LaddaB.Location = new System.Drawing.Point(366, 383);
            this.LaddaB.Name = "LaddaB";
            this.LaddaB.Size = new System.Drawing.Size(75, 23);
            this.LaddaB.TabIndex = 17;
            this.LaddaB.Text = "Ladda";
            this.LaddaB.UseVisualStyleBackColor = true;
            this.LaddaB.Click += new System.EventHandler(this.LaddaB_Click);
            // 
            // openFileDialog1
            // 
            this.openFileDialog1.FileName = "openFileDialog1";
            // 
            // KorTestB
            // 
            this.KorTestB.Location = new System.Drawing.Point(479, 383);
            this.KorTestB.Name = "KorTestB";
            this.KorTestB.Size = new System.Drawing.Size(75, 23);
            this.KorTestB.TabIndex = 18;
            this.KorTestB.Text = "Starta Test";
            this.KorTestB.UseVisualStyleBackColor = true;
            this.KorTestB.Click += new System.EventHandler(this.KorTestB_Click);
            // 
            // RensaB
            // 
            this.RensaB.Location = new System.Drawing.Point(282, 383);
            this.RensaB.Name = "RensaB";
            this.RensaB.Size = new System.Drawing.Size(75, 23);
            this.RensaB.TabIndex = 19;
            this.RensaB.Text = "Rensa";
            this.RensaB.UseVisualStyleBackColor = true;
            this.RensaB.Click += new System.EventHandler(this.RensaB_Click);
            // 
            // MotorLB
            // 
            this.MotorLB.FormattingEnabled = true;
            this.MotorLB.Items.AddRange(new object[] {
                    "På",
                    "Av",
                    "Fel"});
            this.MotorLB.Location = new System.Drawing.Point(654, 354);
            this.MotorLB.Name = "MotorLB";
            this.MotorLB.SelectionMode = System.Windows.Forms.SelectionMode.None;
            this.MotorLB.Size = new System.Drawing.Size(134, 49);
            this.MotorLB.TabIndex = 20;
            // 
            // VentilLB
            // 
            this.VentilLB.FormattingEnabled = true;
            this.VentilLB.Items.AddRange(new object[] {
                    "Öppen",
                    "Stängd",
                    "Fel"});
            this.VentilLB.Location = new System.Drawing.Point(654, 274);
            this.VentilLB.Name = "VentilLB";
            this.VentilLB.SelectionMode = System.Windows.Forms.SelectionMode.None;
            this.VentilLB.Size = new System.Drawing.Size(134, 49);
            this.VentilLB.TabIndex = 21;
            this.VentilLB.SelectedIndexChanged += new System.EventHandler(this.VentilLB_SelectedIndexChanged);
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(651, 258);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(33, 13);
            this.label4.TabIndex = 22;
            this.label4.Text = "Ventil";
            // 
            // label7
            // 
            this.label7.AutoSize = true;
            this.label7.Location = new System.Drawing.Point(651, 338);
            this.label7.Name = "label7";
            this.label7.Size = new System.Drawing.Size(34, 13);
            this.label7.TabIndex = 24;
            this.label7.Text = "Motor";
            // 
            // Namn
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.label7);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.VentilLB);
            this.Controls.Add(this.MotorLB);
            this.Controls.Add(this.RensaB);
            this.Controls.Add(this.KorTestB);
            this.Controls.Add(this.LaddaB);
            this.Controls.Add(this.StopTestB);
            this.Controls.Add(this.BeskrivningTB);
            this.Controls.Add(this.Beskrivning);
            this.Controls.Add(this.label5);
            this.Controls.Add(this.ProjektnamnTB);
            this.Controls.Add(this.SparaB);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.PulsintervalTB);
            this.Controls.Add(this.TimeTB);
            this.Controls.Add(this.WaterflowTB);
            this.Controls.Add(this.SkapaTestB);
            this.Controls.Add(this.TestTable1);
            this.Name = "Namn";
            this.Text = "Form1";
            ((System.ComponentModel.ISupportInitialize)(this.TestTable1)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

#endregion

        private System.Windows.Forms.DataGridView TestTable1;
        private System.Windows.Forms.Button SkapaTestB;
        private System.Windows.Forms.TextBox WaterflowTB;
        private System.Windows.Forms.TextBox TimeTB;
        private System.Windows.Forms.TextBox PulsintervalTB;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.FontDialog fontDialog1;
        private System.Windows.Forms.Button SparaB;
        private System.Windows.Forms.SaveFileDialog saveFileDialog1;
        private System.Windows.Forms.TextBox ProjektnamnTB;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.Label Beskrivning;
        private System.Windows.Forms.RichTextBox BeskrivningTB;
        private System.Windows.Forms.Button StopTestB;
        private System.Windows.Forms.Button LaddaB;
        private System.Windows.Forms.OpenFileDialog openFileDialog1;
        private System.Windows.Forms.Button KorTestB;
        private System.Windows.Forms.Button RensaB;
        private System.Windows.Forms.DataGridViewTextBoxColumn ProjektnamnT;
        private System.Windows.Forms.DataGridViewTextBoxColumn WaterflowT;
        private System.Windows.Forms.DataGridViewTextBoxColumn TimeT;
        private System.Windows.Forms.DataGridViewTextBoxColumn PulsintervalT;
        private System.Windows.Forms.DataGridViewTextBoxColumn BeskrivningT;
        private System.Windows.Forms.CheckedListBox MotorLB;
        private System.Windows.Forms.CheckedListBox VentilLB;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.Label label7;
    }
}

