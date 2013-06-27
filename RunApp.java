import javax.swing.JOptionPane;

public class RunApp {
  
	public static String version_api="1.0";
	private static WinLogin inicioSilb;
	
	public static void main(String[] ar) {
        WelSilb();
        setInicioSilb(new WinLogin());

        return;
    }

	public static void WelSilb() {
        JOptionPane.showMessageDialog(null, "Beinvenidos a Silbido", "Silbido"+version_api, JOptionPane.INFORMATION_MESSAGE);
        return;
    }

	public static WinLogin getInicioSilb() {
		return inicioSilb;
	}

	public static void setInicioSilb(WinLogin inicioSilb) {
		RunApp.inicioSilb = inicioSilb;
	}
	
}
