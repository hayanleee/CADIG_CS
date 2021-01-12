Module CATPtoWrl

    Sub Main(ByVal cmdArgs() As String)
        Dim filePath, fileName As String

        Try
            If cmdArgs.Length > 0 Then
                filePath = cmdArgs(0)
                fileName = cmdArgs(1)
            End If

            If filePath IsNot Nothing And fileName IsNot Nothing Then
                Dim CATIA As Object
                CATIA = CreateObject("Catia.Application")
                CATIA.Visible = False
                Dim fullPath
                fullPath = filePath & "\" & fileName
                If Dir(fullPath) <> "" Then
                    ' transfor CATP* to wrl
                    Dim Doc
                    Doc = CATIA.Documents.Open(fullPath)
                    Dim partDocument1
                    partDocument1 = CATIA.ActiveDocument
                    Dim wrlName, tmpName
                    tmpName = CATIA.ActiveDocument.Name
                    wrlName = Left(tmpName, tmpName.LastIndexOf("."))
                    CATIA.DisplayFileAlerts = False
                    partDocument1.ExportData(filePath & "\" & wrlName & ".wrl", "wrl")
                    CATIA.ActiveDocument.Close()
                End If
            End If
        Catch err As Exception
            Console.WriteLine("error!")
            Console.WriteLine(err)
            'Console.ReadKey(True)
        End Try

    End Sub

End Module