# Como descobrir qual o endereço primário e secundário de um usuário?

Date: 2013-07-22 19:15:36

Categories: Exchange, Exchange 2000, Exchange 2003, Exchange 2007, Exchange 2010, Exchange 5.5

---

<p>Preciso saber na linha de comando abaixo qual é o endereço primário, e qual é o secundário, como faço?</p>
<blockquote>
<pre style="text-align: left;">[PS] C:&gt;get-mailbox guilherme.lima@solucoesms.com.br |fl emailaddresses
EmailAddresses : {smtp:guilherme.lima@solucoesms.com.br, SMTP:guilherme.lima@solucoesms.com.br}</pre>
</blockquote>
<p style="text-align: left;">Simples!<br />
O SMTP é o endereço primário (isso mesmo, em maiúculos), e o secundário é o smtp (em minúsculos). Sempre existirá apenas um SMTP, mas podem existir tantos smtp&#8217;s ou endereços secudários quantos forem necessários.</p>
<p style="text-align: left;">Enjoy!</p>
