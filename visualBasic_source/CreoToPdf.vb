Module CreoToPdf

    Sub Main()
        Dim asyncConnection As pfcls.IpfcAsyncConnection = Nothing 'conn
        Dim cAC As pfcls.CCpfcAsyncConnection
        Dim session As pfcls.IpfcBaseSession
        Dim tModel As pfcls.IpfcModel

        Try
            Console.WriteLine("1")
            cAC = New pfcls.CCpfcAsyncConnection 'asynconn
            cAC = CreateObject("pfcls.pfcAsyncConnection")
            asyncConnection = cAC.Connect("", "", "", 5)
            session = asyncConnection.Session

            Dim descModel As pfcls.IpfcModelDescriptor
            Dim expdf As pfcls.IpfcPDFExportInstructions
            Dim pdfopt As pfcls.IpfcPDFOption
            Dim EpfcPDFOPT_LAUNCH_VIEWER As Boolean
            Dim model As pfcls.IpfcModel

            Console.WriteLine("2")
            EpfcPDFOPT_LAUNCH_VIEWER = False
            'descModel = (New pfcls.CCpfcModelDescriptor).Create(pfcls.EpfcModelType.EpfcMDL_DRAWING, "D:\draw_yura\19ECO0363_LOCK부 형상 변경\050_wp_2m_hsg_a_b.drw.2", Nothing)
            descModel = (New pfcls.CCpfcModelDescriptor).Create(pfcls.EpfcModelType.EpfcMDL_DRAWING, "D:\draw_yura\19ECO0363_LOCK부 형상 변경\220226_27_050_wp_2f_assy_a_b_cu.drw.7", Nothing)
            expdf = (New pfcls.CCpfcPDFExportInstructions).Create()
            pdfopt = (New pfcls.CCpfcPDFOption).Create()
            pdfopt.OptionValue = (New pfcls.CMpfcArgument).CreateBoolArgValue(EpfcPDFOPT_LAUNCH_VIEWER)
            expdf.FilePath = "D:\hayan_vb\test\test.pdf"
            tModel = session.CurrentModel
            Console.WriteLine("3")
            tModel.Export("D:\hayan_vb\test\test.pdf", CType(expdf, pfcls.IpfcExportInstructions))
            Console.WriteLine("4")
        Catch ex As Exception
            Console.WriteLine("error!")
            'MsgBox(ex.Message.ToString + Chr(13) + ex.StackTrace.ToString)
        Finally
            Console.WriteLine("finally")
            asyncConnection.Disconnect(2)
        End Try
        Console.ReadKey(True)
    End Sub

End Module
