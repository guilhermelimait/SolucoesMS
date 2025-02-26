# Como Exportar e Importar regras de transporte do Exchange?

Date: 2020-08-03 09:50:07

Categories: Exchange, Exchange 2010, Exchange 2013, Exchange 2016, Exchange 2019, Exchange Online

---

<p>Durante uma migração, as vezes é necessário exportar e importar as regras de troca de mensagens que os servidores possuem para garantir a segurança dos clientes finais. Utilize o seguinte código para Exportar e Importar as regras:</p>
<p>Exportar as regras de trasnsporte:</p>
<pre class="brush: powershell; title: ; notranslate" title="">$file = Export-TransportRuleCollection; Set-Content -Path &quot;C:\temp\Rules.xml&quot; -Value $file.FileData -Encoding Byte</pre>
<p>Importar as regras de trasnsporte:</p>
<pre class="brush: powershell; title: ; notranslate" title="">&#x5B;Byte&#x5B;]]$Data = Get-Content -Path &quot;C:\temp\Rules.xml&quot; -Encoding Byte -ReadCount 0; Import-TransportRuleCollection -FileData $Data</pre>
<p>Enjoy!</p>
