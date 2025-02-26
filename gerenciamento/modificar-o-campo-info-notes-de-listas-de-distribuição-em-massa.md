# Modificar o campo INFO (NOTES) de listas de distribuição em massa

Date: 2015-10-20 14:24:01

Categories: Exchange, Exchange 2007, Exchange 2010, Exchange 2013, Gerenciamento

---

<p>Olá galerê,</p>
<p style="text-align: justify;">Mais uma solução simples e efetiva pra inserir/modificar o conteúdo do campo INFO ou NOTES das listas de distribuição da sua empresa. Para isso, faremos a importação dos dados à partir de um CSV e alterar o conteúdo em conseguinte.</p>
<p>1- Crie um arquivo chamado ChangeDL.ps1 com o seguinte conteúdo:</p>
<blockquote>
<pre>.\ChangeDLList.csv | % {Set-ADGroup $_ -replace @{info="|MAIL_OUT|"}}</pre>
</blockquote>
<p>2- Crie um arquivo chamado ChangeDLList.csv com o alias das listas de distribuição que precisam ser modificadas.</p>
<p>Enjoy! 🙂</p>
<p>&nbsp;</p>
