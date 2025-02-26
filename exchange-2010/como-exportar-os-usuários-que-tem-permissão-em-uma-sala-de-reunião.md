# Como exportar os usuários que tem permissão em uma sala de reunião?

Date: 2016-05-19 16:51:26

Categories: Exchange 2010

---

<p>Que tal exportar os usuários que tem acesso à criar novos eventos em uma sala de reunião? Sim, sei que é possível qualquer um fazer isso, mas em alguns casos os recursos são bloqueados para apenas alguns usuários. Para isso, se precisar exportar quem tem ou não permissão utilize o código abaixo:</p>
<p>&nbsp;</p>
<blockquote>
<pre><span style="color: #000000;">Get-CalendarProcessing "HO Meeting Room 1" | Select-Object -ExpandProperty:bookinpolicy | Select Name
</span></pre>
</blockquote>
<p>&nbsp;</p>
<p>Espero que tenha ajudado!<br />
Enjoy!</p>
