# Como descobrir se o circular logging está ativado em uma database?

Date: 2013-07-12 17:29:21

Categories: Exchange 2007, Exchange 2010

---

<p style="text-align: justify;">Dúvida simples que pode ser feita por uma linha de comando no nosso Exchange Management Shell. O circular logging é indicado para a seguinte situção: se você tem um banco que cresce muito porém não tem espaço para os logs, ele deve ser ativado e terá suas informações sobrescritas sempre que necessário. A desativação desse processo deve ser observada juntamente a sua arquitetura de backup que irá ser diretamente afetada em um full backup. Chega de conversa, qual o comando?</p>
<blockquote><p>[PS] C:&gt;Get-MailboxDatabase | where {$_.CircularLoggingEnabled -eq $true}Name Server Recovery ReplicationType<br />
&#8212;- &#8212;&#8212; &#8212;&#8212;&#8211; &#8212;&#8212;&#8212;&#8212;&#8212;<br />
Mailbox Database 02 EX1 False Remote<br />
Mailbox Database 04 EX2 False None</p></blockquote>
<p style="text-align: justify;">E como habilitar o circular logging?</p>
<blockquote>
<pre>Set-MailboxDatabase NOMEDADATABASE -CircularLoggingEnabled $true
</pre>
</blockquote>
