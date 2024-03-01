-- Create view vhistoricalpricereporting 
-- as 


SELECT 

 ----FACT TABLE ATTRIBUTES
    HIST.FactID,
    HIST.DATE,
    HIST.[Open],
    HIST.HIGH,
    HIST.LOW,
    HIST.[CLOSE],
    HIST.AdjClose,
    HIST.Volume,

    
    ----DIM SECURITY ATTRIBUTES
    SECURITY.Company,
    SECURITY.Symbol,
    SECURITY.Industry,
    SECURITY.IndexWeighting,

    ----DIM EXCHANGE ATTRIBUTES
    EXC.Symbol AS EXCHANGE

FROM [DBO].[FactPrices_Daily] AS HIST

    INNER JOIN [DBO].[dimSecurity] AS SECURITY
    on hist.[SecurityID] = SECURITY.ID

    INNER JOIN [DBO].[dimExchange] as EXC
    on SECURITY.ExchangeID = EXC.ID 

-- select top(100) * from [dbo].dimSecurity

-- GO