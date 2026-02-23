from solid_principles_py.srp import demo as srp_demo
from solid_principles_py.ocp import demo as ocp_demo
from solid_principles_py.lsp import demo as lsp_demo
from solid_principles_py.isp import demo as isp_demo
from solid_principles_py.dip import demo as dip_demo


def main() -> None:
    """Run all SOLID principle demonstrations."""
    demos = [srp_demo, ocp_demo, lsp_demo, isp_demo, dip_demo]
    for demo in demos:
        demo()


if __name__ == "__main__":
    main()
