 select pv.pedido_venda_id, pv.pedido_venda_numero, c.cliente_nome
    from pedido.tb_pedido_venda as pv
    left join pedido.tb_pedido_venda_endereco as pe on (pv.pedido_venda_endereco_entrega_id=pe.pedido_venda_endereco_id)
    left join cliente.tb_cliente as c on (pv.cliente_id=c.cliente_id) 
    where pe.pedido_venda_endereco_nome not ilike c.cliente_nome 
    and pe.pedido_Venda_endereco_nome=(
    	select cliente_nome from cliente.tb_cliente where conta_id=175058 and cliente_id!=c.cliente_id)
    and pv.conta_id=175058


  