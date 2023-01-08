Attribute VB_Name = "Module1"
Sub ticker_macro()
Dim totalvolume As Double
For Each ws In ThisWorkbook.Worksheets

lRow = ws.Cells(Rows.Count, 1).End(xlUp).Row
Columnticker = 1
columnvolume = 7
columnopenprice = 3
columncloseprice = 6
counter = 1
Row = 2
totalvolume = 0
ws.Cells(1, 9).Value = "Ticker"
ws.Cells(1, 10).Value = "Yearly Change"
ws.Cells(1, 11).Value = "Percent Change"
ws.Cells(1, 12).Value = "Total Stock Volume"

For i = 2 To lRow

If ws.Cells(i + 1, Columnticker).Value <> ws.Cells(i, Columnticker).Value Then
    Ticker = ws.Cells(i, Columnticker).Value
    counter = counter + 1
    openprice = ws.Cells(counter, columnopenprice).Value
    closeprice = ws.Cells(i, columncloseprice).Value
    For j = counter To i
                totalvolume = totalvolume + ws.Cells(j, columnvolume).Value
    Next j
    YearlyChange = closeprice - openprice
    PercentChange = YearlyChange / openprice
    ws.Cells(Row, 9).Value = Ticker
    ws.Cells(Row, 10).Value = YearlyChange
    ws.Cells(Row, 11).Value = PercentChange
    ws.Cells(Row, 11).NumberFormat = "0.00%"
    ws.Cells(Row, 12).Value = totalvolume
    Row = Row + 1
    totalvolume = 0
    YearlyChange = 0
    PercentChange = 0
    counter = i
End If
Next i

SummaryLastRow = ws.Cells(Rows.Count, "I").End(xlUp).Row
        For i = 2 To SummaryLastRow
            If ws.Cells(i, 10) > 0 Then
                ws.Cells(i, 10).Interior.ColorIndex = 4
            Else
                ws.Cells(i, 10).Interior.ColorIndex = 3
            End If
            If ws.Cells(i, 11) > 0 Then
                ws.Cells(i, 11).Interior.ColorIndex = 4
            Else
                ws.Cells(i, 11).Interior.ColorIndex = 3
            End If

        Next i

Increase = 0
Decrease = 0
greatestvolume = 0
ws.Cells(2, 14).Value = "Greatest % Increase"
ws.Cells(3, 14).Value = "Greatest % Decrease"
ws.Cells(4, 14).Value = "Greatest Total Volume"
ws.Cells(1, 15).Value = "Ticker"
ws.Cells(1, 16).Value = "Value"

For i = 3 To SummaryLastRow
    previousi = i - 1
    currentpercent = ws.Cells(i, 11).Value
    previouspercent = ws.Cells(previousi, 11).Value
    currentvolume = ws.Cells(i, 12).Value
    previousvolume = ws.Cells(previousi, 12).Value
    If Increase > currentpercent And Increase > previouspercent Then
    Increase = Increase
    ElseIf currentpercent > Increase And currentpercent > previouspercent Then
    Increase = currentpercent
    increaseticker = ws.Cells(i, 9).Value
    ElseIf previouspercent > Increase And previouspercent > currentpercent Then
    Increase = previouspercent
    increaseticker = ws.Cells(previousi, 9).Value
    End If
    If Decrease < currentpercent And Decrease < previouspercent Then
    Decrease = Decrease
    ElseIf currentpercent < Decrease And currentpercent < previouspercent Then
    Decrease = currentpercent
    decreaseticker = ws.Cells(i, 9).Value
    ElseIf previouspercent < Decrease And previouspercent < currentpercent Then
    Decrease = previouspercent
    decreaseticker = ws.Cells(previousi, 9).Value
    End If
    If greatestvolume > currentvolume And totalvolume > previousvolume Then
    greatestvolume = greatestvolume
    ElseIf currentvolume > greatestvolume And currentvolume > previousvolume Then
    greatestvolume = greatestvolume
    greatestvalueticker = ws.Cells(i, 9).Value
    ElseIf previousvolume > greatestvolume And previousvolume > currentvolume Then
    greatestvolume = previousvolume
    greatestvalueticker = ws.Cells(previousi, 9).Value
    End If
Next i
    ws.Cells(2, 15).Value = increaseticker
    ws.Cells(3, 15).Value = decreaseticker
    ws.Cells(4, 15).Value = greatestvalueticker
    ws.Range("P2").NumberFormat = "0.00%"
    ws.Range("P3").NumberFormat = "0.00%"
    ws.Cells(2, 16).Value = Increase
    ws.Cells(3, 16).Value = Decrease
    ws.Cells(4, 16).Value = greatestvolume
Next ws
End Sub
