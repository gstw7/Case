SELECT A.ID_PESSOA, A.NM_PESSOA, B.NU_MES, B.NU_ANO, C.VL_VENDA, D.DS_CIDADE
FROM d_Pessoa A, d_Tempo B, f_Vendas C, d_Loja D
WHERE B.NU_MES = 'Janeiro' AND B.NU_ANO = '2020' AND D.DS_CIDADE = ' Ceará (CE)';