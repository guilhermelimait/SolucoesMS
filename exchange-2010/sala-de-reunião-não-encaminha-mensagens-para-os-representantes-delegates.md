# Sala de reunião não encaminha mensagens para os Representantes (Delegates)

Date: 2016-09-16 14:24:45

Categories: Exchange, Exchange 2010

---

<p>Problema simples porém chatinho, após adicionar a representante da sala, ao convidar a sala para ser o recurso de uma reunião, a representante não recebe mensagens para confirmar o agendamento.</p>
<p>Para esse problema, uma simples solução (fonte original logo abaixo):</p>
<blockquote><p>Resource General:<br />
&#8211; Enable the Resource Booking Attendant (if the Resource Booking Attendant is disabled, the recource booking settings incl. delegates are disabled too)</p>
<p>Resource Policy:<br />
&#8211; Specify the delegates<br />
&#8211; Enable &#8220;Forward meeting requests to delegates&#8221;</p>
<p>Recource In-Policy Requests:<br />
&#8211; In-Policy requests autom. approved-&gt;Selected recipients-&gt;don&#8217;t select any recipients<br />
&#8211; In-Policy requests subject to approval-&gt;All users</p>
<p>Recource Out-of-Policy Requests:<br />
&#8211; Users allowed out-of-policy requests-&gt;All users (if you want to allow all users send out-of-policy requests&#8230;)</p>
<p>This configuration will forward every meeting request to the delegates. The meeting organizer will be notified that the meeting request is pendig approval.</p></blockquote>
<p>&nbsp;</p>
<p>Enjoy!<br />
Fonte: <a href="https://social.technet.microsoft.com/Forums/exchange/en-US/6faace3b-06e6-4cac-95a6-13de06a97713/exchange-2010-delegates-not-getting-forwarded-meeting-requests?forum=exchange2010" target="_blank">Technet</a></p>
