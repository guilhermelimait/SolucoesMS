# Dar permissão de edição no calendário da sala de reunião

Date: 2019-04-23 15:13:06

Categories: Exchange 2013, Exchange 2016, Office 365

---

<p style="text-align: justify;">Olá pessoal, em uma nova requisição, o cliente gostaria de fazer edições do tipo, arrastar uma reunião entre salas em seu calendário. Assim, o recurso seria alterado automaticamente. Para isso, uma permissão simples precisa ser inserida:</p>
<pre>add-mailboxfolderpermission -identity (RoomMailbox):\calendar -user ("UserMailboxAddress") -accessrights Editor</pre>
<p>Caso receba um erro de que o calendar não existe, o usuário deve estar usando outra lingua nas configurações regionais, para isso, no Brasil, utilize o \calendário como o padrão.</p>
<p style="text-align: justify;">Esse tipo de permissão, é a mesma atividade de entrar no calendário da sala de reunião e dar a permissão de editor para o usuário. Detalhe, deve ser feito em todas as salas de reunião que o usuário tem acesso.</p>
<p>Enjoy!</p>
