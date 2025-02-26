# Usuário externo não consegue adicionar reunião na agenda de uma sala de reuniões

Date: 2019-05-08 15:32:21

Categories: Exchange, Exchange 2013, Exchange 2016, Office 365

---

<p style="text-align: justify;">Hi all,<br />
Tive um caso interessante ao ver que usuários externos da corporação ao convidar um recurso (sala de reunião) a reunião era confirmada porém a agenda não mostrava o compromisso. Para resolver esse problema, utilize o comando abaixo:</p>
<pre><span style="color: #ff0000;">Set-CalendarProcessing "&lt;Room Name&gt;" –ProcessExternalMeetingMessages $True</span></pre>
<p>Enjoy!</p>
