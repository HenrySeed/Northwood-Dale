
def pane(player):
    health = player.health
    max_health = player.max_health
    health_ratio = health/max_health
    
    exp = player.exp
    nec_level = player.next_level
    exp_ratio = exp/nec_level
    
    pane_lines = []
    
    pane_lines.append('  Health [{0:14}]  '.format(int(health_ratio * 14) * '#'))
    pane_lines.append('             {0} / {1}       '.format(health, max_health))
    pane_lines.append('')
    pane_lines.append('  EXP    [{0:14}]  '.format(int(exp_ratio * 14) * '#'))
    pane_lines.append('           {0} / {1}         '.format(exp, nec_level))
    pane_lines.append('')
    pane_lines.append('')
    pane_lines.append('  (I)nventory              ')
    pane_lines.append('  (M)ap                    ') 
    pane_lines.append('  (Q)uests                 ')
    pane_lines.append('  (C)haracter              ')  
    pane_lines.append('  (H)elp                   ') 
    pane_lines.append('')
    
    return pane_lines
    
    
