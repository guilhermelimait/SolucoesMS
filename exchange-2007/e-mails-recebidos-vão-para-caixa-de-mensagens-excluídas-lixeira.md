# E-mails recebidos vão para caixa de Mensagens Excluídas (lixeira)

Date: 2015-05-29 14:03:17

Categories: Exchange 2007, Exchange 2010

---

<p style="text-align: justify;">Nesse caso inédito para mim, todas as mensagens que eram recebidas eram direcionadas para a pasta de Mensagens excluídas (lixeira) ao invés da Caixa de Entrada como de praxe. Esse estranho evento me fez procurar por várias soluções sendo que a que mais comum era aplicada apenas ao Exchange 2007 (<a href="https://support.microsoft.com/en-us/kb/959960" target="_blank">https://support.microsoft.com/en-us/kb/959960</a>). Nesse caso, ela não poderia ser aplicada pois o servidor é Exchange 2010. Após várias pesquisas apliquei o seguinte comando:</p>
<blockquote>
<pre>Get-CalendarProcessing USER | fl Delete*
DeleteAttachments : True
DeleteComments : True
DeleteSubject : True
DeleteNonCalendarItems : True</pre>
</blockquote>
<p style="text-align: justify;">O argumento <strong>DeleteNonCalendarItems</strong> configurado como <strong>True</strong> é o responsável por mover todas as mensagens recebidas serem movidas para a pasta de Mensagens Excluídas ao invés da Caixa de Entrada como padrão. Para solucionar, precisamos apenas mudar o argumento assim como informado abaixo.</p>
<blockquote>
<pre>Get-CalendarProcessing USER | Set-CalendarProcessing -DeleteNonCalendarItems: $False -AutomateProcessing AutoUpdate

</pre>
</blockquote>
<p>Enjoy!</p>
