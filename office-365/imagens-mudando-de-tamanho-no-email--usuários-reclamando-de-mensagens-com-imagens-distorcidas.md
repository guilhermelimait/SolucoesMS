# Imagens mudando de tamanho no email / usuários reclamando de mensagens com imagens distorcidas

Date: 2018-02-15 16:39:12

Categories: Office 365

---


<p>Ao enviar novos emails as imagens que estavam no corpo da mensagem acabavam ficando desproporcionais após o envio. Problema estranho mas foi possível identificar o problema ao verificar a codificação do corpo da mensagem.</p>



<p>Para verificar a codificação, abra a mensagem &gt; botão direito &gt; exibir codificação. Abaixo o resultado:</p>



<pre class="wp-block-code"><code>&lt;html&gt;&lt;head&gt;

&lt;style type="text/css" style="display:none;"&gt;&lt;!-- P {margin-top:0;margin-bottom:0;} --&gt;&lt;/style&gt;
&lt;/head&gt;
&lt;body dir="ltr"&gt;
&lt;div id="divtagdefaultwrapper" style="font-size:12pt;color:#000000;font-family:Calibri,Helvetica,sans-serif;" dir="ltr"&gt;
&lt;p style="margin-top:0;margin-bottom:0"&gt;&lt;img size="1647605" contenttype="image/png" id="img652417" style="max-width: 99.9%; user-select: none;" tabindex="0" src="cid:15df5d0e-15c0-4185-b09d-aea499f6ecaf"&gt;&lt;br&gt;
&lt;br&gt;
&lt;/p&gt;
&lt;/div&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>



<p>O campo que diz &#8220;max-width: 99.9%&#8221; é o nosso problema, para resolvê-lo faremos a utilização de um procedimento desenvolvido pela Microsoft. Segundo ela, após a alteração do uso do Word como editor padrão para o Outlook 2010 esse problema pode vir a acontecer. A solução segue abaixo:</p>



<figure class="wp-block-image"><img decoding="async" src="cid:15df5d0e-15c0-4185-b09d-aea499f6ecaf" alt="" /></figure>



<p>HKEY_CURRENT_USER\Software\Microsoft\Office\xx.0\Word\Options</p>



<ul class="wp-block-list">
<li>On the <strong>Edit</strong> menu, point to <strong>New</strong>, and then click <strong>DWORD Value</strong>.</li>
<li>Type DontUseScreenDpiOnOpen, and then press Enter.</li>
<li>In the Details pane, right-click DontUseScreenDpiOnOpen, and then click <strong>Modify</strong>.</li>
<li>In the <strong>Value data</strong> box, type 1, and then click <strong>OK</strong>.</li>
<li>Exit Registry Editor.</li>
</ul>



<figure class="wp-block-image"><img decoding="async" src="cid:15df5d0e-15c0-4185-b09d-aea499f6ecaf" alt="" /></figure>



<p>Fonte: <a href="https://support.microsoft.com/en-us/help/3042197/graphics-file-attachment-grows-larger-in-the-recipient-s-email-message">https://support.microsoft.com/en-us/help/3042197/graphics-file-attachment-grows-larger-in-the-recipient-s-email-message</a></p>



<p>&nbsp;</p>



<figure class="wp-block-image"><img decoding="async" src="cid:15df5d0e-15c0-4185-b09d-aea499f6ecaf" alt="" /></figure>
