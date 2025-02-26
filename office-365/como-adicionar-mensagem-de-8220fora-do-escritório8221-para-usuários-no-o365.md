# Como adicionar mensagem de &#8220;Fora do escritório&#8221; para usuários no O365

Date: 2018-01-31 18:27:27

Categories: Exchange, Office 365

---

<p style="text-align: justify;">Caso necessite adicionar informações no e-mail de resposta automática para os usuários que estão fora do escritório sem ter que dar permissões à sua caixa de admin, acessar via web e inserir as informações, utilize o comando abaixo que é simples e efetivo.</p>
<blockquote>
<pre style="text-align: justify;"><span style="color: #ff0000;">Set-MailboxAutoReplyConfiguration -Identity user@mailbox.com -AutoReplyState Enabled -ExternalMessage "Estou fora do escritório" -InternalMessage "Estou fora do escritório" -endtime 2018/02/20</span></pre>
</blockquote>
<p style="text-align: justify;">Caso queira desabilitar a função utilize o seguinte comando:</p>
<div class="entry-content">
<div id="wpshdo_2" class="wp-synhighlighter-outer">
<div id="wpshdi_2" class="wp-synhighlighter-inner">
<blockquote>
<pre><span style="color: #ff0000;">Set<span class="sy0">-</span>MailboxAutoReplyConfiguration <span class="sy0">-</span>Identity user@mailbox.com <span class="sy0">-</span>AutoReplyState Disabled</span></pre>
</blockquote>
</div>
</div>
</div>
<p>Enjoy!</p>
