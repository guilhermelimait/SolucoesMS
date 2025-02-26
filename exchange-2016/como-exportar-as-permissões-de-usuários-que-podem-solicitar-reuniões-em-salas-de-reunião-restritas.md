# Como exportar as permissões de usuários que podem solicitar reuniões em Salas de Reunião restritas

Date: 2017-09-01 13:03:00

Categories: Exchange, Exchange 2007, Exchange 2010, Exchange 2013, Exchange 2016

---

<p>Chega a ser complicado de explicar em poucas palavras mas este comando irá exportar as permissões de usuários que estão autorizados a solicitar reuniões em recursos como Salas de Reunião restritas do Exchange.</p>
<p>Para isso, use o comando a seguir:</p>
<pre>Get-CalendarProcessing &lt;EMAILDASALADEREUNIAO&gt; |Select-Object -ExpandProperty:bookinpolicy |select name</pre>
