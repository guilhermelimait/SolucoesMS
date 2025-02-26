# Como identificar quantas mailbox foram criadas nas últimas 24h?

Date: 2014-06-18 12:40:13

Categories: Exchange 2010

---

<p>Olá pessoal, Mais uma solução simples e bacana é essa em que é identificada as últimas contas de mailbox criadas nas últimas 24h, acompanhe:</p>
<pre class="bbcode_code">Get-Mailbox -Server EXMB1 | Where {$_.WhenCreated -gt (Get-Date).AddDays(-1)}</pre>
<p>Caso queira aumentar esse range, apenas troque a data para o número de dias necessários, por exemplo, últimos 7 dias.</p>
<pre class="bbcode_code">Get-Mailbox -Server EXMB1 | Where {$_.WhenCreated -gt (Get-Date).AddDays(-7)}</pre>
<p>Enjoy!</p>
