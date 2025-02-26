# Como configurar uma conta cross domain com o linked master account?

Date: 2018-02-07 14:44:13

Categories: Exchange, Exchange 2010

---


<p>Caso precise configurar uma conta que seja cross domain, ou seja, um usuário no AD que não possui Exchange, com uma conta de AD que possui Exchange, execute o seguinte comando:</p>



<pre class="wp-block-verse">set-user -id ContaADAtual - LinkedMasterAccount domíniolegado\usuariolegado -LinkedDomainController FQDNdomaincontroller</pre>



<p></p>
