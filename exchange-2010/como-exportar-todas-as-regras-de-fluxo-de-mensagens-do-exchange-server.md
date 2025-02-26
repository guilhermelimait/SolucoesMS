# Como exportar todas as regras de fluxo de mensagens do Exchange Server?

Date: 2020-03-26 14:59:28

Categories: Exchange, Exchange 2010, Exchange 2013, Exchange 2016, Exchange 2019

---

<p>Opa! Momentos de crise, isolamento, mas continuamos à mil na procura de soluções. Para exportar as regras do seu Exchange server siga os comandos abaixo:</p>
<pre class="brush: powershell; title: ; notranslate" title="">$file = Export-TransportRuleCollection
Set-Content -Path &quot;C:\Rules.csv&quot; -Value $file.FileData -Encoding Byte</pre>
<p>Para importar esses dados no servidor novo, execute o seguinte comando:</p>
<pre class="brush: powershell; title: ; notranslate" title="">$Data = Get-Content -Path &quot;C:\Rules.csv&quot; -Encoding Byte -ReadCount 0
Import-TransportRuleCollection -FileData $Data</pre>
<p>Enjoy!</p>
