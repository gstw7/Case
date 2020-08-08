SELECT A.ID_PESSOA, A.NM_PESSOA, B.NU_VENDA, max(C.DT_REF) as Ultima_venda
FROM d_Pessoa A, f_Vendas B, d_Tempo C
GROUP BY ID_PESSOA;