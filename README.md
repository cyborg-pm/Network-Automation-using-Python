<div class="repo-description">
  <h1>📌 Network Automation Toolkit</h1>
  <p>Python scripts to automate Cisco network device configurations (VLANs, backups, ACLs) using Netmiko, NAPALM, and Ansible. Ideal for network engineers learning infrastructure-as-code.</p>

  <h2>Key Features</h2>
  <ul>
    <li><strong>VLAN Provisioning</strong>: Auto-configure VLANs via Python (<code>netmiko</code>).</li>
    <li><strong>Config Backups</strong>: Daily device config backups with timestamping.</li>
    <li><strong>ACL Deployment</strong>: Ansible playbooks for bulk ACL updates.</li>
    <li><strong>Multi-Vendor Support</strong>: Works with Cisco IOS (extensible to other vendors).</li>
  </ul>

  <h2>Tech Stack</h2>
  <ul>
    <li>Python 3 (Netmiko, NAPALM)</li>
    <li>Ansible (for playbook automation)</li>
    <li>Cisco IOS (tested on 2911/2960 in GNS3/Packet Tracer)</li>
  </ul>

  <h2>Use Cases</h2>
  <ul>
    <li>Reduce manual network configuration errors.</li>
    <li>Scale repetitive tasks across devices.</li>
    <li>Learn network automation best practices.</li>
  </ul>

  <h2>Quick Start</h2>
  <pre><code># Install dependencies
pip install netmiko napalm ansible

# Run VLAN provisioning
python scripts/vlan_provision.py</code></pre>
</div>

