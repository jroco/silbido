//import java.awt.*;
import java.awt.Container;
import java.awt.FlowLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

//import java.awt.event.*;
import javax.swing.*;

public class WinLogin extends JFrame
{
  private static final long serialVersionUID = 1L;
	private JTextField UserAcct;
	private JPasswordField UserPswd;
	
    // configurar GUI
    public WinLogin()
    {
       super( "Silbido Login Window");

       Container contenedor = getContentPane();      
       contenedor.setLayout( new FlowLayout() );
 
       UserAcct = new JTextField( "Cuenta Twitter" );
       contenedor.add( UserAcct );

       // crear campo de contraseña con texto predeterminado
       UserPswd = new JPasswordField( "Password" );
       contenedor.add( UserPswd );
 
       // registrar manejadores de eventos
       ManejadorCampoTexto manejador = new ManejadorCampoTexto();
       UserAcct.addActionListener( manejador );
       UserPswd.addActionListener( manejador );
       
       ManejadorClicsRaton handMouse = new ManejadorClicsRaton();
       UserAcct.addMouseListener( handMouse );
       UserPswd.addMouseListener( handMouse );
       
       this.setBounds(250,250,500,300);
       this.setVisible(true);
    }
    
    // clase interna privada para el manejo de eventos
    private class ManejadorCampoTexto implements ActionListener
    {
       // procesar eventos de campo de texto
       public void actionPerformed( ActionEvent evento )
       {
          String cadena = "";
 
          // el usuario oprimió Intro en objeto JTextField UserAcct
          if ( evento.getSource() == UserAcct ){
             cadena = "UserAcct: " + evento.getActionCommand();
 
          // el usuario oprimió Intro en objeto JTextField UserPswd
          }
          else if ( evento.getSource() == UserPswd ){
             cadena = "UserPswd: " + 
          new String( UserPswd.getPassword() );
          }
 
          JOptionPane.showMessageDialog( null, cadena,"Resultados",JOptionPane.CANCEL_OPTION);
 
       } // fin del método actionPerformed
       
    } // fin de la clase interna privada ManejadorCampoTexto
    
    private class ManejadorClicsRaton extends MouseAdapter {

       // manejar evento de clic del ratón y determinar cuál botón se oprimió
       public void mouseClicked(MouseEvent evento)
       {
		   if(evento.getSource() == UserAcct )
		   {
			   UserAcct.setText("");
		   }
		   
		   if(evento.getSource() == UserPswd )
		   {
			   UserPswd.setText("");
		   }

       } // fin del método mouseClicked

    } // fin de la clase interna privada ManejadorClicsRaton

}
