# Como remover mensagens presas na Queue pelo Powershell?

Date: 2018-11-20 15:29:37

Categories: Exchange 2010, Exchange 2013

---

<p>Se você precisar remover mensagens da queue aqui está um simples comando.</p>
<blockquote>
<pre>Remove-Message -Server servidorexchange -Filter {FromAddress -eq "email@dominio.com"} -WithNDR $false</pre>
</blockquote>
<p>Enjoy!</p>
