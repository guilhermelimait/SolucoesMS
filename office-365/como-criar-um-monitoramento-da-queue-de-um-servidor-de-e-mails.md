# Como criar um monitoramento da queue de um servidor de e-mails

Date: 2018-09-05 10:46:07

Categories: Office 365

---



Após migrar para o O365, algumas empresas ainda precisam deixar algumas aplicações locais que não são compatíveis com o O365. Para isso, os admins geralmente criam um servidor com IIS para envio de mensagens e também precisam monitorá-lo para evitar problemas. Para isso, monitore a fila usando o seguinte script em seu monitoramento.




<pre class="wp-block-preformatted">$queue = (Get-ChildItem E:\SMTPLogs\Mailroot\Queue | Measure-Object).Count
if ($queue -gt 1000) {set-content -path "C:\MonitoraQueue\result_fila.txt" -value "Fila Grande"}
else {set-Content -path "C:\MonitoraQueue\result_fila.txt" -value "Fila OK"}</pre>












Enjoy!

