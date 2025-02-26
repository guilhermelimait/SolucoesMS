# Como criar um disclaimer de autoassinatura?

Date: 2014-07-09 13:41:16

Categories: Exchange 2007, Exchange 2010, Exchange 2013

---

<p>Para criar um disclaimer de autoassinatura é preciso criar uma nova transport role que tenha algum parâmetro de comparação para a aplicação da disclaimer. Para o nosso exemplo, todos os usuários de mailbox que contiverem a palavra &#8220;Empresa&#8221; no campo Company receberá o disclaimer.</p>
<blockquote>
<pre>New-TransportRule -Name 'Auto-Assinatura' -Comments 'Disclaimer for outgoing mails' -Priority '3' -Enabled $true -SenderADAttributeContainsWords 'Company:Empresa' -ApplyHtmlDisclaimerLocation 'Append' -ApplyHtmlDisclaimerText '&lt;p&gt;&lt;b&gt;&lt;i&gt;AVISO LEGAL&lt;/p&gt;&lt;/b&gt;&lt;/i&gt; "As informações existentes nesta mensagem e nos arquivos anexados têm caráter confidencial e são para uso restrito. A utilização, divulgação, cópia ou distribuição desta mensagem, ou parte dela, por qualquer pessoa diferente do destinatário é proibida, sujeitando o infrator às sanções legais. Se esta mensagem foi recebida por engano, favor excluí-la e informar ao remetente pelo endereço eletrônico acima. Agradecemos sua cooperação."' -ApplyHtmlDisclaimerFallbackAction 'Wrap' -ExceptIfSentToScope 'InOrganization'</pre>
</blockquote>
<p>Espero que tenha ficado fácil para você pois a aplicação é bem simples e pode ser utilizado outro campo como referência também.<br />
Boa sorte!</p>
