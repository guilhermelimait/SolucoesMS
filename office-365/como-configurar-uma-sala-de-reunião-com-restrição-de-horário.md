# Como configurar uma sala de reunião com restrição de horário

Date: 2018-07-03 18:33:59

Categories: Exchange, Office 365

---

<p>Olá, que tal mais um desafio interessante? Dessa vez, faremos uma restrição de horário para uma sala de reuniões que precisa ser agendada apenas entre as 8h30 e 16h30. Para isso, utilize do comando a seguir:</p>
<pre>Set-MailboxCalendarConfiguration -Identity saladereuniao@dominio.com.br -WorkingHoursStartTime 08:30:00 -WorkingHoursEndTime 16:30:00 -WorkingHoursTimeZone "E. South America Standard Time"</pre>
<p>Repararam que ela possui um campo para definição do TimeZone? Caso precise verificar essas informações de horário e timezone já definidos, utilize o comando abaixo:</p>
<pre>Get-MailboxCalendarConfiguration saladereuniao@dominio.com.br |select *working*</pre>
<p>E caso precise descobrir quais tipos de TimeZone estão disponíveis, use o seguinte comando:</p>
<pre>$TimeZone = Get-ChildItem "HKLM:\Software\Microsoft\Windows NT\CurrentVersion\Time zones" | foreach {Get-ItemProperty $_.PSPath}; $TimeZone | sort Display | Format-Table -Auto PSChildname,Display</pre>
<p>Espero ter ajudado!</p>
<p>Fonte: <a href="https://docs.microsoft.com/en-us/powershell/module/exchange/client-access/set-mailboxcalendarconfiguration?view=exchange-ps">Microsoft</a></p>
<p>Fonte2: <a href="https://docs.microsoft.com/en-us/powershell/module/exchange/client-access/set-mailboxcalendarconfiguration?view=exchange-ps">Microsoft</a></p>
<p>&nbsp;</p>
<p>&nbsp;</p>
